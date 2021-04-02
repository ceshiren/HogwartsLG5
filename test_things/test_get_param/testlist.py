
#列表推导式
import datetime
import os
import time

# list3=[i**2 for i in range(1,4) if i !=1]
# print(list3)
# list4=[i*j for i in range(1,4) for j in range(1,5)]
# print(list4.sort())
# tuple1 =1,2,4
# print(type(tuple1))
# list4.pop(2)
# print(list4)
# set1 =set()
# print(set1,type(set1))
# print(os.getcwd())
# # os.path.abspath()
# print(time.strftime("%Y %m %d - %H %M %S", time.localtime(time.time())))
# print(time.localtime(time.time()))
# threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
# print(threeDayAgo)
# print(datetime.datetime.now())


# :两个无序数组合成一个，并去重，最后从小到大排序
list1=[1,3,6,3,21,56,8]
list2=[3,52,62,2,7,8]
#union intersection difference
set1=set(list1).union(set(list2))
set1.pop()
print(set1)
list1=list(set1)
list1.sort()
print(list1)
