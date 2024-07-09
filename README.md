

# DynamicPoseAnalyzer

DynamicPoseAnalyzer is a web application developed using Flask and Mediapipe for real-time pose estimation. It allows users to compare their live poses with a reference image, calculating similarity indices based on both Euclidean distances and angular differences between key landmarks.

## Features

- **Real-time Pose Estimation**: Utilizes Mediapipe to detect and visualize poses in real-time from a webcam feed.
- **Pose Comparison**: Compares live poses with a reference image to calculate similarity indices.
- **Angular and Euclidean Similarity**: Computes angular differences and Euclidean distances to quantify pose similarity.
- **Web Interface**: Provides a user-friendly web interface using Flask for easy interaction.

## Installation

To run PoseVision locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/PoseVision.git
   cd PoseVision
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Start the Flask development server:

   ```
   python app.py
   ```

4. Open a web browser and go to `http://localhost:5000` to view and interact with PoseVision.

To integrate MongoDB with your Flask application for storing pose estimation data, you'll need to follow these steps:

1. **Install MongoDB and PyMongo**:
   Make sure you have MongoDB installed on your machine. You can download it from [here](https://www.mongodb.com/try/download/community). Install the PyMongo library using pip:

   ```sh
   pip install pymongo
   ```

2. **Set Up MongoDB Connection in Flask**:
   Create a new file `db.py` to handle the MongoDB connection.

3. **Modify `app.py` to Include Database Operations**:
   Update your Flask application to save pose estimation results to the MongoDB database.
   ```

3. **Upload an Image and Start Pose Estimation**:
   Access your web app, upload an image, and start the pose estimation process. The results will be saved to your MongoDB database.

This setup will allow you to store the pose estimation results in a MongoDB collection named `pose_results`. You can further expand the functionality by adding more fields to the database documents or creating more complex queries and analyses.
## Usage

- Upload a reference image using the form provided the upload.py
- Allow access to your webcam to capture live pose estimations.
- View live pose comparisons with the reference image, including similarity indices.



## Applications



### Fitness and Sports

- **Fitness Tracking**: Monitor and analyze fitness routines by comparing proper form with reference poses.
- **Sports Coaching**: Assist coaches in analyzing and improving athletes' techniques by providing real-time feedback on posture and movement.
- **Physical Therapy**: Aid physical therapists in evaluating and tracking patients' progress in performing therapeutic exercises accurately.

### Dance and Performing Arts

- **Choreography**: Assist choreographers in designing and refining dance routines by visualizing and comparing movements.
- **Performance Analysis**: Evaluate dancers' performances by comparing their poses with ideal forms, helping them achieve better accuracy and expressiveness.

### Education and Research

- **Biomechanics Research**: Support biomechanics researchers in studying human movement patterns and posture dynamics.
- **Educational Tools**: Provide interactive learning tools for students and educators in anatomy, kinesiology, and sports science.

### Gaming and Virtual Reality

- **Motion Capture**: Integrate with gaming and virtual reality systems for immersive experiences and realistic avatar animations.
- **Gesture Recognition**: Enable gesture-based controls and interactions in gaming applications and virtual environments.

### Healthcare and Assistive Technologies

- **Rehabilitation**: Assist in rehabilitation programs by monitoring patients' movements and providing feedback on corrective exercises.
- **Assistive Devices**: Enable the development of assistive technologies that respond to users' gestures and postures.





## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


