from imutils.video import VideoStream
import imutils
import time
import cv2
# initialize the motion saliency object and start the video stream

class Saliency:
  def __init__(self):
    pass

  def myfunc(self, path):

    self.path = path
    self.saliency = None
    self.vs = cv2.VideoCapture(self.path)

    # Check if camera opened successfully
    if (self.vs.isOpened() == False):
        print("Error opening video  file")
        return
    time.sleep(2.0)

    while(self.vs.isOpened()):
        # grab the frame from the threaded video stream and resize it
        # to 500px (to speedup processing)
        self.ret, self.frame = self.vs.read()
        if not self.ret:
            break
        self.frame = cv2.resize(self.frame, (500, 500))

        # if our saliency object is None, we need to instantiate it

        if self.saliency is None:
            self.saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
            self.saliency.setImagesize(self.frame.shape[1], self.frame.shape[0])
            self.saliency.init()
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        (self.success, self.saliencyMap) = self.saliency.computeSaliency(self.gray)
        self.saliencyMap = (self.saliencyMap * 255).astype("uint8")
        # print(type(self.saliencyMap))
        # print("Shape of array: ", self.saliencyMap.shape)
        #break
        # display the image to our screen
        cv2.imshow("Map", self.saliencyMap)
        self.key = cv2.waitKey(1) & 0xFF
        if self.key == ord("q"):
            break
    cv2.destroyAllWindows()



