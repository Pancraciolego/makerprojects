import cv2
import numpy as np

image = cv2.imread("Blocks.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_color = np.array([0, 130, 70])   # lower bound of color in HSV
upper_color = np.array([10, 255, 255]) # upper bound of color in HSV
mask = cv2.inRange(hsv, lower_color, upper_color)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    rect = cv2.minAreaRect(contour) 
    x,y = rect[1]
    print(x,y)
    if (x>300) and (y>300):  # checks if box is large enough
        print("2",rect[2])
        print("rect",rect)
        angle = rect[-1]
        if angle<-45:
            angle+=90
        print("angle",rect[-1])  # outpus angles
        box = cv2.boxPoints(rect)  # makes the boxes
        box = np.int64(box)
        cv2.drawContours(image, [box], 0, (0,255,0),2)
        cv2.imshow("Outlined Image", image)
        cv2.waitKey(0)


#cv2.drawContours(image, contours, -1, (250, 250, 250), 2)  # green outline

# Show the output
cv2.imshow("Outlined Image", image)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()