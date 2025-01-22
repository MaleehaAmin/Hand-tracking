import math
import csv


import pandas

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang
    """""
    if ang < 0:
        ang = ang + 360
        ang = ang * (math.pi / 180)
    else:
        ang = ang * (math.pi / 180)
        return ang
"""



header = ['x1','y1','x2','y2','x3','y3','x4','y4','x5','y5','bend']
data = pandas.read_csv('experiment103march2022_1646292917.33.csv', names=header)


for idx in range(data.shape[0]):
    angle=[]
    angle1 = getAngle([data.iloc[idx]['y1'],data.iloc[idx]['x1']] , [data.iloc[idx]['y2'],data.iloc[idx]['x2']], [data.iloc[idx]['y3'],data.iloc[idx]['x3']] )
    angle2 = getAngle([data.iloc[idx]['y2'], data.iloc[idx]['x2']], [data.iloc[idx]['y3'], data.iloc[idx]['x3']],
                      [data.iloc[idx]['y4'], data.iloc[idx]['x4']])
    angle3 = getAngle([data.iloc[idx]['y3'], data.iloc[idx]['x3']], [data.iloc[idx]['y4'], data.iloc[idx]['x4']],
                      [data.iloc[idx]['y5'], data.iloc[idx]['x5']])
    angle1=angle1/57
    angle2=angle2/57
    angle3=angle3/57

    angle.append(angle1)
    angle.append(angle2)
    angle.append(angle3)



    with open('cal_angles.csv', 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerow(angle)


# print(type(angle))
# print(angle)

