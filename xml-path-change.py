import xml.dom.minidom
import os
path ="C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\Annotations"  # xml文件存放路径
sv_path = "C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\Annotations"  # 修改后的xml文件存放路径
files = os.listdir(path)
for xmlFile in files:
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
    root = dom.documentElement  # 得到文档元素对象
    item = root.getElementsByTagName('path')  # 获取path这一node名字及相关属性值
    for i in item:
        i.firstChild.data = '"C:\\Users\\zz\\Desktop\\deep learning\\yolov5-v5.0\\yolov5-master\\data\\images'  # xml文件对应的图片路径
        with open(os.path.join(sv_path, xmlFile), 'w') as fh:
            dom.writexml(fh)
