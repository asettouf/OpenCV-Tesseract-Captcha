#/usr/bin/env python

import numpy as np
import cv2
import cv2.cv as cv
import tesseract

image = cv2.imread("temp.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5,5),0)
(T, tresh) = cv2.threshold(blurred, 155,255, cv2.THRESH_BINARY)


cv2.imshow("Avg GaussianBlur",np.hstack([blurred, tresh]))
cv2.waitKey(0)

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT) 
api.SetPageSegMode(tesseract.PSM_SINGLE_BLOCK)
height1,width1 = tresh.shape
channel1=1
image = cv.CreateImageHeader((width1,height1), cv.IPL_DEPTH_8U, channel1)
cv.SetData(image, tresh.tostring(),tresh.dtype.itemsize * channel1 * (width1))
tesseract.SetCvImage(image,api)
text=api.GetUTF8Text()
conf=api.MeanTextConf()
image=None
print "..............."
print "Ocred Text: %s"%text
print "Cofidence Level: %d %%"%conf