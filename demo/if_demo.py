'''
条件判断
'''
#----------------------------------------------------------------------
age = 18
if age<18:
    print("未满十八岁禁止关注")
else:
    print("您满十八岁了,可以看一些东西了")
#----------------------------------------------------------------------
# age = input("请输入您出生的年份：")#age为字符串需要转为数字
# age = int(age)
age = 1992
if age>2000:
    print('您不是00后')
elif age < 2000 and age > 1990:
    print('您是90后')
else:
    print('您是老年人')
#----------------------------------------------------------------------
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
import math
height = 1.75
weight = 80.5
bmi = math.sqrt(weight / height)
# print(bmi)
# for x in range(10):
#     print(x)
#----------------------------------------------------------------------
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])
# 0 Google
# 1 Baidu
# 2 Runoob
# 3 Taobao
# 4 QQ
print(list(range(5)))#[0, 1, 2, 3, 4]
#----------------------------------------------------------------------
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
#----------------------------------------------------------------------
#计算1-10000的和
sum = 0;
for i in range(1,10001):
    sum = sum+i
print(sum)
#----------------------------------------------------------------------
L = ['Bart', 'Lisa', 'Adam']
for i in range(len(L)):
    print("hello,"+L[i])
#----------------------------------------------------------------------
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
#----------------------------------------------------------------------
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
#----------------------------------------------------------------------

#----------------------------------------------------------------------

#----------------------------------------------------------------------

#----------------------------------------------------------------------