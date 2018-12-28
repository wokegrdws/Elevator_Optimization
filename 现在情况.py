import random
import numpy as np

STUNUM = 12 #电梯满载人数
FLOLOW = 4 #最低第4层
FLOHIGH = 18 #最高第18层
TRIP_DURATION = 2 #上升时间
STOP_DURATION = 8 #停止时间
OUT_DURATION = 4 #平均出电梯时间

#创建学生类
class Student(object):
    def __init__(self, num, floor, time):
        self.num = num
        self.floor = floor
        self.time = time

#去除列表内重复元素函数
def deleteDuplicatedElementFromList(list):
        list.sort();
        print("sorted list:%s" % list)
        length = len(list)
        lastItem = list[length - 1]
        for i in range(length - 2,-1,-1):
                currentItem = list[i]
                if currentItem == lastItem:
                        list.remove(currentItem)
                else:
                        lastItem = currentItem
        return list

#写成一个函数，方便后面调用很多次
def calculatemean():
    #12个学生
    stu0 = Student(0, random.randint(FLOLOW, FLOHIGH), 0)
    stu1 = Student(1, random.randint(FLOLOW, FLOHIGH), 0)
    stu2 = Student(2, random.randint(FLOLOW, FLOHIGH), 0)
    stu3 = Student(3, random.randint(FLOLOW, FLOHIGH), 0)
    stu4 = Student(4, random.randint(FLOLOW, FLOHIGH), 0)
    stu5 = Student(5, random.randint(FLOLOW, FLOHIGH), 0)
    stu6 = Student(6, random.randint(FLOLOW, FLOHIGH), 0)
    stu7 = Student(7, random.randint(FLOLOW, FLOHIGH), 0)
    stu8 = Student(8, random.randint(FLOLOW, FLOHIGH), 0)
    stu9 = Student(9, random.randint(FLOLOW, FLOHIGH), 0)
    stu10 = Student(10, random.randint(FLOLOW, FLOHIGH), 0)
    stu11 = Student(11, random.randint(FLOLOW, FLOHIGH), 0)

    #12个对象存放于元组（不可更改）
    stu = (stu0, stu1, stu2, stu3, stu4, stu5, stu6, stu7, stu8, stu9, stu10, stu11)

    #对象的层数存放与列表
    list = [stu[0].floor, stu[1].floor, stu[2].floor, stu[3].floor, stu[4].floor, stu[5].floor, stu[6].floor, stu[7].floor, stu[8].floor, stu[9].floor, stu[10].floor, stu[11].floor]

    #查找各个楼层下了多少人
    myset = set(list)
    for item in myset:
        print("第%d层下了%d个学生" %(item,list.count(item)))

    #去除重复的楼层后，排序得到电梯停留楼层，list已经改变了
    deleteDuplicatedElementFromList(list)

    #打印电梯停留的楼层
    print('电梯停留的楼层是', list)

    #将每一个学生的层数i和电梯停留的楼层在表中的位置j对比，计算每个学生的等待时间并打印
    for i in range(STUNUM):
        for j in range(len(list)):
            if stu[i].floor == list[j]:
                stu[i].time = (stu[i].floor - 1) * TRIP_DURATION + (j + 1) * STOP_DURATION - (STOP_DURATION - OUT_DURATION)
        print('第',stu[i].num,'号学生的等待时间是', stu[i].time)

    #取平均
    sum_time = 0
    for i in range(STUNUM):
        sum_time = sum_time + stu[i].time

    mean_time = sum_time / STUNUM
    return mean_time

#调用无数次，取平均作为仿真结果
add_time = 0
times = 10000
for i in range(times):
    add_time = add_time + calculatemean()
ave_time = add_time / times
print('学生的平均等待时间是', ave_time)