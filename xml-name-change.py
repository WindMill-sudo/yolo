import glob
from xml.etree import ElementTree as ET

# 批量读取Annotations下的xml文件
xml_dir = r'/data/Annotations'
xml_list = glob.glob(xml_dir + '/*.xml')
for xml in xml_list:
    print(xml)
    per = ET.parse(xml)
    p = per.findall('/object')

    for one in p:  # 找出person节点
        child = one.getchildren()[0]  # 找出person节点的子节点
        if child.text == 'nodule':
            child.text = 'tumor'

    per.write(xml)
    print(child.tag, ':', child.text)

