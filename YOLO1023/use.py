from detfunc import detect_func
color,box,conf = detect_func('data/images/000279.png')
print('颜色：',color)
print('box：',box)
print('置信度：',conf)

#交并比计算
from IoU import box_iou_xywh
bbox1 = [100., 100., 200., 200.]
bbox2 = [120., 120., 220., 220.]
iou = box_iou_xywh(bbox1, bbox2)
print(iou)

bbox =[]
n = 1
for i in box:
    for j in box[n:]:
        bbox.append(box_iou_xywh(i,j))
    n = n + 1
print(bbox)



