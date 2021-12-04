# import xml.dom.minidom
# import os
# path = 'C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\Annotations'     # xml文件存放路径
# sv_path = 'C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\Annotations'  # 修改后的xml文件存放路径
# files = os.listdir(path)
#
# for xmlFile in files:
#     dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
#     root = dom.documentElement  # 得到文档元素对象
#     names = root.getElementsByTagName('filename')
#     a, b = os.path.splitext(xmlFile)  # 分离出文件名a
#     for n in names:
#         n.firstChild.data = a + '.bmp'
#     with open(os.path.join(sv_path, xmlFile), 'w') as fh:
#         dom.writexml(fh)

#!/usr/bin/python
 # -*- coding: UTF-8 -*-

import os
import shutil

src_dir_path = 'D:\\yolo-defect\\yolov5-6.0\\data\\Annotations'        # 源文件夹

to_dir_path = 'D:\\yolo-defect\\yolov5-6.0\\data\new'         # 存放复制文件的文件夹

key = 'bubble-gum'                 # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中

if not os.path.exists(to_dir_path)
    print("to_dir_path not exist,so create the dir")
    os.mkdir(to_dir_path,1)
if os.path.exists(src_dir_path):
    print("src_dir_path exitst")
    for file in os.listdir(src_dir_path):
        # is file
        if os.path.isfile(src_dir_path+'/'+file):
            if key in file:
                print('找到包含"'+key+'"字符的文件,绝对路径为----->'+src_dir_path+'/'+file)
                print('复制到----->'+to_dir_path+file)
                shutil.copy(src_dir_path+'/'+file,to_dir_path+'/'+file)

