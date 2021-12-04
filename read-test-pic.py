import cv2

file = 'D:\yolo-defect\yolov5-6.0\data'
image_ids = open('%s/ImageSets/x.txt' % file).read().strip().split()
list_file = open('%s/xml.txt' % file).read().strip().split()
# print(list_file)
for image in range(len(list_file)):
    IMG = cv2.imread(list_file[image])
    # cv2.imshow('display', IMG)
    # cv2.waitKey(500)
    # cv2.destroyAllWindows()
    print(IMG)
    cv2.imwrite('%s/new/%s.xml' % (file, image_ids[image]), IMG)

