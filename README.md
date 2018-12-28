# 大运村电梯调度优化

大运村最高的楼层达到18层，对于住在高楼层的同学来说，大运村公寓最烦心的事情就是上下楼了。电梯上行的过程中需要在不同的低楼层停留多次，才能到达自己的楼层，下行也同理。

特别是在中午上楼的时候，电梯口会挤满下了课回寝室的同学。不仅电梯内会在上行的过程中很挤，不断在各个楼层停留，而且很多同学甚至挤不上第一班电梯，需要等待下一班。也有同学宁愿会选择步行走上十几层楼梯。中午时分这个拥挤的过程至少会持续20分钟，而同学们被浪费的时间是非常多的。

为了减少同学们中午等待电梯时间的浪费，本文对中午高峰期电梯上行的调度用python进行了模拟仿真，并提出了优化方案。

## 现状分析
### 先决条件

通过对大运村真实情况以及同学们心理的观察，本文将中午高峰期电梯上楼的真实情况简化，抽象出以下先决条件:

+ 电梯最低在1层，最高在18层，所有同学只在1层上电梯
+ 各个寝室分布在2层至18层
+ 住在第2、3层的同学选择不坐电梯
+ 同学只愿意去往自己住的楼层，而不愿意去相邻楼层再步行至自己楼层
+ 同学去往不同楼层的可能性是均匀分布的
+ 电梯每上行一层花费时间2秒
+ 电梯每停一次(加减速、开门、进出、关门)花费时间8秒
+ 同学平均在电梯停下后4秒离开电梯
+ 共有两个电梯，每个电梯每次最多承载12人
+ 高峰期上行的电梯始终能满载

### 现状仿真

将先决条件用程序语言表示。在这里两个电梯是完全一样的，不必分开考虑。通过随机数随机产生每个同学的目标楼层，对每次电梯的上行进行仿真。本文采用每个同学在 整个过程中花费时间的平均值来描述某种调度方法的效率。重复以上仿真若干次，可以提高结果的精度。整体算法的伪代码如Algorithm1。

<p align="center">
    <img src="https://github.com/wokegrdws/Markdown-Images/blob/master/大运村电梯优化图集/alg.png"  width=70% height=70%>
    <p align="center">
        <em></em>
    </p>
</p>

这里的输入是：
```python
import random
import numpy as np

STUNUM = 12 #电梯满载人数
FLOLOW = 4 #最低第4层
FLOHIGH = 18 #最高第18层
TRIP_DURATION = 2 #上升时间
STOP_DURATION = 8 #停止时间
OUT_DURATION = 4 #平均出电梯时间
```

每个学生随机均匀目标楼层的产生函数:
```python
for i in range(STUNUM):
    stu[i].floor = random.randint(FLOLOW, FLOHIGH) #产生(包括)最低最高楼层间的随机整数
```

### 现状仿真结果

由于仿真的次数取了times=10,000次，可以确定结果已经非常接近理论值。将每次仿真结果用散点图来表示。
```python
学生的平均等待时间是53.78898333333308
```

<p align="center">
    <img src="https://github.com/wokegrdws/Markdown-Images/blob/master/大运村电梯优化图集/现在情况结果.png"  width=80% height=80%>
    <p align="center">
        <em></em>
    </p>
</p>

即，未优化前，中午高峰期大运村电梯上行过程中每个学生平均花费的时间是53.8秒。 我们将以这个未优化的数据为参考标准，衡量下面调度优化方案的效果。

## 单双层优化

本文对两个电梯进行设置:电梯A只能在单数层停留，电梯B只能在双数层停留。

这里将对A、B两个电梯分别进行仿真，将分别得出的结果求平均即可作为最终结果。

每个学生随机均匀**单数**目标楼层的产生函数:
```python
for i in range(STUNUM):
    stu[i].floor = random.randrange(FLOLOW, FLOHIGH, 2)
    stu[i].floor = stu[i].floor + 1
```

每个学生随机均匀**双数**目标楼层的产生函数:
```python
for i in range(STUNUM):
    stu[i].floor = random.randrange(FLOLOW, FLOHIGH + 1, 2)
```

其余不变进行仿真。

**单数**电梯的仿真结果是:
```python
学生的平均等待时间是43.54270000000004
```

**双数**电梯的仿真结果是:
```python
学生的平均等待时间是45.633866666666734
```

<div style="float:left;border:solid 1px 000;margin:2px;"><img src="https://github.com/wokegrdws/Markdown-Images/blob/master/大运村电梯优化图集/奇数情况结果.png"  width="200" height="260" ></div>

<div style="float:left;border:solid 1px 000;margin:2px;"><img src="https://github.com/wokegrdws/Markdown-Images/blob/master/大运村电梯优化图集/偶数情况结果.png" width="200" height="260" ></div>





