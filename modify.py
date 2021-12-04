# import cv2 as cv
# import numpy as np
#
# def video_demo():
#     capture=cv.VideoCapture(0)
#     while(True):
#         ret,frame=capture.read()
#         frame=cv.flip(frame,1)
#         cv.imshow("video",frame)
#         cv.waitKey(500)
#
#
# def get_image_info(image):
#     print(type(image))
#     print(image.shape)
#     print(image.size)
#     print(image.dtype)
#     pixel_data=np.array(image)
#     print(pixel_data)
#
#
# src=cv.imread("C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\ggg\\20210422-161315621-0203001-002659.bmp")
# cv.namedWindow("input image",cv.WINDOW_NORMAL)
# cv.imshow("input image",src)
# #get_image_info(src)
# #green=cv.cvtColor(src,cv.COLOR_BGR2HSV)
# #cv.imwrite("D:/result.png",src)
# #video_demo()
# cv.waitKey(500)
#
# cv.destroyAllWindows()


import os
def myrename(path):
    file_list=os.listdir(path)
    i=1631
    for fi in file_list:
        old_name=os.path.join(path,fi)
        new_name=os.path.join(path,str(i)+".bmp")
        os.rename(old_name,new_name)
        i+=1

if __name__=="__main__":
    path="data/i1"
    myrename(path)

