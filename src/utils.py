import cv2

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

def save_image(save_path, image):
    cv2.imwrite(save_path, image)

def display_image(image, window_name='Image'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()