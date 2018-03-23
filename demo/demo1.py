'''

'''

print('''line1
      line2''')

a='abc'
print(a)
a=1
print(a)

print(9/3)
print(10/3)
print(9//3)
print(10//3)
print(10 % 3)

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print(chr(20013))
print(r'\u4e2d\u6587')
print('\u4e2d\u6587')
#bytes类型的数据用带b前缀的单引号或双引号表示
print(b'ABC')

#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围
# print('中国'.encode('ascii')) 报错
print('ABC'.encode('ascii'))
print('中国'.encode('utf-8'))

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

#%s表示用字符串替换，%d表示用整数替换，%f表示浮点数,%x十六进制整数
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好
#如果只有一个%?，括号可以省略
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
# 不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
