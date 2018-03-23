'''
列表方法测试
'''
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
#---------------------------------------------------------------------
#访问列表中的值
print(list1[0])#Google
print(list2[:2])#[1, 2]
print(list3[2:4])#['c', 'd']
#---------------------------------------------------------------------
#更新列表
list4 = list1[2]
print(list4)#1997
list4 = 2001
print(list4)#2001
#---------------------------------------------------------------------
#删除列表元素
list2 = ['Google', 'Runoob', 1997, 2000]
print (list2)
del list2[2]
print ("删除第三个元素 : ", list2)
#---------------------------------------------------------------------
#Python列表脚本操作符
list2 = ['Google', 'Runoob', 1997, 2000]
print(len(list2))#4
list2 = [1,2,3]
list3 = [4,5,6]
print(list2 + list3)#[1, 2, 3, 4, 5, 6]
print('Hi'*4)#HiHiHiHi
print(3 in [1, 2, 3])#True
for x in [1, 2, 3]: print(x, end=" ")#1 2 3
#---------------------------------------------------------------------
#Python列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
print(L[2])#Taobao
print(L[-2])#Runoob
print(L[1:])#['Runoob', 'Taobao']
#---------------------------------------------------------------------
#嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)#[['a', 'b', 'c'], [1, 2, 3]]
print(x[0])#['a', 'b', 'c']
print(x[1][0]) #1
#----------------------Python列表函数-----------------------------
#列表元素个数 len(list)
print(len(x))#2
print(len(a))#3
#---------------------------------------------------------------------
#max(list)返回列表元素最大值
# print(max(x))#报错TypeError: unorderable types: int() > str()
print(max(a))#c
#---------------------------------------------------------------------
#min(list)返回列表元素最小值
#---------------------------------------------------------------------
#list(seq)将元组转换为列表
aa = (1,2,3,4)
ll = list(aa)
print(ll)#[1, 2, 3, 4]
#---------------------------方法------------------------------------------
#list.append(obj)在列表末尾添加新的对象
list1 = ['Google', 'Runoob', 'Taobao']
list1.append("Baidu")
print(list1)#['Google', 'Runoob', 'Taobao', 'Baidu']
#---------------------------------------------------------------------
#list.count(obj)统计某个元素在列表中出现的次数
print(list1.count("Runoob"))#
#---------------------------------------------------------------------
#list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1 = ['Google', 'Runoob', 'Taobao']
list2 = ['Baidu','Sina']
list1.extend(list2)
print(list1)#['Google', 'Runoob', 'Taobao', 'Baidu', 'Sina']
#---------------------------------------------------------------------
#list.index(obj)从列表中找出某个值第一个匹配项的索引位置
list1 = ['Google', 'Runoob', 'Taobao']
print(list1.index('Taobao'))#2
#---------------------------------------------------------------------
#list.insert(index, obj)将对象插入列表
obj = 'Baidu'
list1.insert(2,obj)
print(list1)#['Google', 'Runoob', 'Baidu', 'Taobao']
#---------------------------------------------------------------------
#list.pop(obj=list[-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list1.pop())#Taobao
list1 = ['Google', 'Runoob', 'Taobao']
print(list1.pop(1))#Runoob
#---------------------------------------------------------------------
#list.remove(obj)移除列表中某个值的第一个匹配项
list1 = ['Google', 'Runoob', 'Taobao']
list1.remove('Runoob')
print(list1)#['Google', 'Taobao']
#---------------------------------------------------------------------
#list.reverse()反向列表中元素
list1 = ['Google', 'Runoob', 'Taobao']
list1.reverse()
print(list1)#['Taobao', 'Runoob', 'Google']
#---------------------------------------------------------------------
#list.sort([func])对原列表进行排序
list1 = ['Google', 'Taobao', 'Runoob']
list1.sort()
print(list1)#['Google', 'Runoob', 'Taobao']
#---------------------------------------------------------------------
#list.clear()清空列表
list1.clear()
print(list1)
#---------------------------------------------------------------------
#list.copy()复制列表
list1 = ['Google', 'Taobao', 'Runoob']
list2 = []
print(list2)
list2 = list1.copy()
print(list2)
