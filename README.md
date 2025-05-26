# Face Detection Application

This project is a simple face detection application that utilizes computer vision techniques to detect faces in images. It is built using Python and leverages popular libraries such as OpenCV and NumPy.

## Project Structure

```
face-detection-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── detector.py      # Contains the FaceDetector class for face detection
│   └── utils.py         # Utility functions for image processing
├── requirements.txt      # Lists the project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/face-detection-app.git
   cd face-detection-app
   ```

2. **Install the required dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the face detection application, execute the following command:

```
python src/main.py
```

Follow the prompts to input the image file path you want to process. The application will detect faces and display the results.

## Face Detection Algorithm

This application uses a pre-trained face detection model based on Haar Cascades or a deep learning model (depending on the implementation in `detector.py`). The `FaceDetector` class is responsible for loading the model, detecting faces in images, and drawing rectangles around detected faces.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.# face-recognition
