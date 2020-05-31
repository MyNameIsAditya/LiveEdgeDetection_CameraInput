import cv2
import numpy as np

def main():
	#Capture the video from a camera input and put it in cap
	#cap contains ret (which indicates if the operation was successful) and frame (a collection of images)
	cap = cv2.VideoCapture(0)
	
	while (True):
		ret, frame = cap.read()
		cv2.imshow("Edge Detection", detectEdges(frame))
		
		#Exit if Enter key is pressed
		if (cv2.waitKey(1) == 13):
			break

	#Closes camera input and windows
	cap.release()
	cv2.destroyAllWindows()  

def detectEdges(frame):
	#Convert to graysclae image
	grayscaleImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#Prepare image with a gaussian blur and remove noise
	blurredImage = cv2.GaussianBlur(grayscaleImage, (5, 5), 0)

	#Detect edges with Canny algorithm
	edgesDetectedImage = cv2.Canny(blurredImage, 10, 70)

	return edgesDetectedImage

main()
