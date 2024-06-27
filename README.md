

# DynamicPoseAnalyzer

PoseVision is a web application developed using Flask and Mediapipe for real-time pose estimation. It allows users to compare their live poses with a reference image, calculating similarity indices based on both Euclidean distances and angular differences between key landmarks.

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

## Usage

- Upload a reference image using the form provided.
- Allow access to your webcam to capture live pose estimations.
- View live pose comparisons with the reference image, including similarity indices.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


