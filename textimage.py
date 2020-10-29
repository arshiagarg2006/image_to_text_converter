import pytesseract as tess
from PIL import Image

import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    img_name = "another.jpg"
    cv2.imwrite(img_name, frame)
    break
cam.release()
cv2.destroyAllWindows()
block = Image.open("another.jpg")
block.show()

tess.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

img = Image.open('another.jpg')

text = tess.image_to_string(img)

print(text)
