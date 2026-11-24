import cv2

img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, result = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Segmented", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
