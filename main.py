import cv2 as c

def getOriginalImage():
	originalImage = c.imread("back.jpg")
	originalImage = c.cvtColor(originalImage,c.COLOR_BGR2GRAY)
	originalImage = c.GaussianBlur(originalImage,(21,21),0)
	return originalImage
	
def getOriginaloriginalVideo():
	originalVideo = c.VideoCapture("video.mp4")
	return originalVideo
	
def getgrayImageImage(imageFrame):
	grayImage = c.cvtColor(imageFrame,c.COLOR_BGR2GRAY)
	grayImage = c.GaussianBlur(grayImage,(21,21), 0)
	return grayImage
	
def getThrehold(diff):
	threshold = c.threshold(diff,30,255,c.THRESH_BINARY)[1]
	threshold = c.dilate(threshold, None, iterations = 2)
	return threshold
	
def displayCountors(contours):
	for everyContour in contours:
			for x in range(50):
				(X,Y,w,h) = c.boundingRect(everyContour)
				c.rectangle(imageFrame,(X,Y),(X+w,Y+h),(0,255,0), 3)

	c.imshow("Tracking Object Movement (Press 'q' to stop)",imageFrame)

def forceQuit():
	keyPressed = c.waitKey(1)
	if keyPressed == ord('q'):
		return 1
	else:
		return 0

if __name__ == "__main__":
	try:
		originalImage = getOriginalImage()
		originalVideo = getOriginaloriginalVideo()

		while True:
			getStatus, imageFrame = originalVideo.read()
			grayImage = getgrayImageImage(imageFrame)

			diff = c.absdiff(originalImage,grayImage)
				
			threshold = getThrehold(diff)


			contours,result = c.findContours(threshold.copy(),c.RETR_EXTERNAL,c.CHAIN_APPROX_SIMPLE)
				
			displayCountors(contours)
				
			if forceQuit() == 1:
				break
	except :
		print("Execution Complete")