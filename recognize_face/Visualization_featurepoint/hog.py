import cv2
output_path="./result.png"
converter = cv2.HOGDescriptor()
img = cv2.imread('test.png')
hog = cv2.HOGDescriptor()
hog = hog.compute(img)
cv2.imwrite(output_path, hog)