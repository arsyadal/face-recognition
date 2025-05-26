import cv2

class FaceDetector:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        self.model = cv2.CascadeClassifier(model_path)

    def detect_faces(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.model.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
        return faces

    def draw_faces(self, image, faces):
        if image is None or faces is None:
            return None
        img_copy = image.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img_copy