import cv2
from detector import FaceDetector
from utils import load_image, save_image, display_image

def main():
    # Initialize the face detector
    face_detector = FaceDetector()
    model_path = "haarcascade_frontalface_default.xml"  # Pastikan file ini ada di folder src
    face_detector.load_model(model_path)

    # Load an image from the user
    image_path = input("Enter the path to the image: ")
    image = load_image(image_path)
    if image is None:
        print("Gambar tidak ditemukan atau gagal dibaca. Cek path dan nama file.")
        return

    # Detect faces in the image
    faces = face_detector.detect_faces(image)
    if faces is None or len(faces) == 0:
        print("Tidak ada wajah terdeteksi pada gambar.")
        return
    else:
        print(f"{len(faces)} wajah terdeteksi.")

    # Draw rectangles around detected faces
    output_image = face_detector.draw_faces(image, faces)
    if output_image is None:
        print("Gagal memproses gambar output.")
        return

    # Save and display the output image
    save_image("output.jpg", output_image)
    print("Hasil disimpan sebagai output.jpg")
    display_image(output_image)

if __name__ == "__main__":
    main()