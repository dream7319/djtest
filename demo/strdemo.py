'''
字符串
'''
var1 = 'hello world'
var2 = 'Runnob'
print(var1[0])#h
print(var2[1:3])#un
print(var2[:3])#Run
print(var1 + var2)
print(var2 * 2)

if 'h' in var1:
    print("h 在var1中")

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
