import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from PIL import Image

picpath = './inputimg/input.png'


def ocrfun():
        try:
                
                #read image
                img = cv2.imread(picpath)

                #convert to gray
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                #apply dilation and erosion to remove noise

                #img = cv2.Canny(img,100,200)

                kernel = np.ones((1,1),np.uint8)
                img = cv2.dilate(img,kernel,iterations = 1)
                img = cv2.erode(img,kernel,iterations = 1)

                #apply threshold to get black and white
                #img =cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

                img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)


                # Write the image after apply opencv to do some ...
                cv2.imwrite("./processedimg/" + "thes.png", img)

                #recognize text with tesseract

                result = pytesseract.image_to_string(Image.open('./processedimg/thes.png'))

                return result
                

        except Exception as ex:
                print(ex)


