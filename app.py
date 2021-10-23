from cv2 import cv2
import numpy as np
import sys

if len(sys.argv) != 2:
    print("Use: python3 app.py <image directory>")
else:
    dir = sys.argv[1]
    img = cv2.imread(dir)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img,9, 250,250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imwrite("image.jpeg", img)
    cv2.imwrite("Edges.jpeg", edges)
    cv2.imwrite("Cartoon.jpeg", cartoon)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    