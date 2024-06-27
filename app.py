from flask import Flask, render_template, Response, jsonify ,request
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

reference_image = cv2.imread(r"C:\Users\adity\Downloads\stock-photo-fitness-male-model-in-studio-2261599187.jpg")
reference_landmarks = None

def get_pose_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    if results.pose_landmarks:
        return results.pose_landmarks
    return None

def draw_landmarks(image, landmarks):
    mp_draw.draw_landmarks(image, landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((255, 0, 255), 2, 2))

def calculate_pose_similarity(landmarks1, landmarks2):
    if not landmarks1 or not landmarks2:
        return float('inf')

    lm1 = np.array([(lm.x, lm.y, lm.z) for lm in landmarks1.landmark])
    lm2 = np.array([(lm.x, lm.y, lm.z) for lm in landmarks2.landmark])

    distances = np.linalg.norm(lm1 - lm2, axis=1)
    mean_distance = np.mean(distances)

    return mean_distance

def calculate_angle(point1, point2, point3):
    a = np.array([point1.x, point1.y])
    b = np.array([point2.x, point2.y])
    c = np.array([point3.x, point3.y])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

def calculate_angular_similarity(landmarks1, landmarks2):
    if not landmarks1 or not landmarks2:
        return float('inf')

    angles1 = []
    angles2 = []

    landmark_triplets = [
        (11, 13, 15),
        (12, 14, 16),
        (23, 25, 27),
        (24, 26, 28)
    ]

    for triplet in landmark_triplets:
        angles1.append(calculate_angle(landmarks1.landmark[triplet[0]], landmarks1.landmark[triplet[1]], landmarks1.landmark[triplet[2]]))
        angles2.append(calculate_angle(landmarks2.landmark[triplet[0]], landmarks2.landmark[triplet[1]], landmarks2.landmark[triplet[2]]))

    angle_differences = np.abs(np.array(angles1) - np.array(angles2))
    mean_angle_difference = np.mean(angle_differences)

    return mean_angle_difference

def calculate_pose_similarity_index(euclidean_similarity, angular_similarity, max_distance):
    normalized_euclidean = euclidean_similarity / max_distance 
    normalized_angular = angular_similarity / 180.0  

    similarity_index = (0.5 * normalized_euclidean) + (0.5 * normalized_angular)
    return (1 - similarity_index)

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    cap = cv2.VideoCapture(0)
    global reference_landmarks
    reference_landmarks = get_pose_landmarks(reference_image)
    max_distance = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (600, 400))
        live_landmarks = get_pose_landmarks(frame)

        if live_landmarks:
            draw_landmarks(frame, live_landmarks)

            euclidean_similarity = calculate_pose_similarity(reference_landmarks, live_landmarks)
            if euclidean_similarity > max_distance:
                max_distance = euclidean_similarity

            angular_similarity = calculate_angular_similarity(reference_landmarks, live_landmarks)
            pose_similarity_index = calculate_pose_similarity_index(euclidean_similarity, angular_similarity, max_distance)

            cv2.putText(frame, f"Pose Similarity Index: {pose_similarity_index:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        ref_img = np.zeros_like(frame)
        ref_img.fill(255)
        if reference_landmarks:
            draw_landmarks(ref_img, reference_landmarks)

        combined_frame = np.hstack((frame, ref_img))

        ret, buffer = cv2.imencode('.jpg', combined_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
