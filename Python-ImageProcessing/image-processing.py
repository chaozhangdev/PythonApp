import cv2
import glob

def batch_resize():
    images = glob.glob("*.jpg")
    for image in images:
        img = cv2.imread(image, 1)
        x = int (img.shape[1] / 2)
        y = int (img.shape[0] / 2)
        re = cv2.resize(img, (x,y))
        cv2.imshow("Hey", re)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.imwrite("resized_"+image,re)

def resize(name):
    img = cv2.imread(name, 1)
    x = int (img.shape[1] / 2)
    y = int (img.shape[0] / 2)
    re = cv2.resize(img, (x,y))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized.jpg", re)


class image_processing:

    def resize(value):
        x = int (img.shape[0]/value)
        y = int (img.shape[1]/value)
        re = cv2.resize(img, (x,y))
        return re

    def darker(value):
        for k in range(3):
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    data = img[i][j][k] - value
                    if data < 0:
                        data = 0 
                    if data > 255:
                        data = 255
                    img[i][j][k] = data

    def brighter(value):
        for k in range(3):
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    data = img[i][j][k] + value
                    if data < 0:
                        data = 0 
                    if data > 255:
                        data = 255
                    img[i][j][k] = data

    def invert():
        for k in range(3):
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    data = 255 - img[i][j][k] 
                    if data < 0:
                        data = 0 
                    if data > 255:
                        data = 255
                    img[i][j][k] = data
    



if __name__ == "__main__":

    img = cv2.imread("qq1.jpg", 1)
    image_processing.invert()
    cv2.imshow("processed_image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()