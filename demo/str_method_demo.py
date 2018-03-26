'''
字符串方法测试
'''
var1 = "hello"
var2 = "Runnob"
# 将字符串的第一个字符转换为大写
print(var1.capitalize())
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#	center(width, fillchar)
print(var2.center(20,'*'))
# str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
#count(str, beg= 0,end=len(string))
print(var2.count('n',0,3))
#------------------------decode----------------------------
#encode(encoding='UTF-8',errors='strict')
#bytes.decode(encoding="utf-8", errors="strict")
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，
# 这个 bytes 对象可以由 str.encode() 来编码返回
str = "菜鸟教程";
#以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，
# 除非 errors 指定的是'ignore'或者'replace'
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
#----------------------------------------------------
#endswith(suffix, beg=0, end=len(string))
#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，
# 如果是，返回 True,否则返回 False.
str='Runoob example....wow!!!'
suffix='!!'
print(str.endswith(suffix))
print(str.endswith(suffix,20))
suffix='run'
print (str.endswith(suffix))
print (str.endswith(suffix, 0, 19))
#----------------------------------------------------
#expandtabs(tabsize=8)
#把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是8
str = "this is\tstring example....wow!!!"
print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print (r"使用16个空格替换 \t 符号: " +  str.expandtabs(16))
#----------------------------------------------------
#	find(str, beg=0 end=len(string))
#检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，
# 如果包含返回开始的索引值，否则返回-1
str1 = "Runoob example....wow!!!"
str2 = "exam";
print(str1.find(str2,0,20))#7
print(str1.find(str2,0,3))#-1
#----------------------------------------------------
#index(str, beg=0, end=len(string))
#跟find()方法一样，只不过如果str不在字符串中会报一个异常.
print(str1.index(str2))
# print(str1.index(str2,0,3))#异常
#----------------------------------------------------
#如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
#isalnum()
str = "ABCabc123"
print(str.isalnum())#True
str='ab!'
print(str.isalnum())#False
#----------------------------------------------------
#isalpha()
#如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
print("abcABC".isalpha())
#----------------------------------------------------
#isdigit()如果字符串只包含数字则返回 True 否则返回 False..
print("-------->","123".isdigit())
#----------------------------------------------------
#islower()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，
#则返回 True，否则返回 False
print("abcd".islower())
#----------------------------------------------------
#isnumeric()如果字符串中只包含数字字符，则返回 True，否则返回 False
print('123'.isnumeric())
print('四'.isnumeric())#True
print('中'.isnumeric())#False
print("Ⅶ".isnumeric())#罗马数字
#----------------------------------------------------
#isspace()如果字符串中只包含空白，则返回 True，否则返回 False.
print(" ".isspace())
print("\t".isspace())#True
#----------------------------------------------------
#istitle()如果字符串是标题化的(见 title())则返回 True，否则返回 False
#即：首字母均为大写
str = "This Is String Example...Wow!!!"
print (str.istitle())#True
str = "This is string example....wow!!!"
print (str.istitle())#False
#----------------------------------------------------
#isupper()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print("A123".isupper())#True
print("Abc".isupper())#False
#----------------------------------------------------
#join(seq)以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
str={'a', 'b', 'c'}
print("-".join(str))
str=('a','b','c')
print("-".join(str))
#----------------------------------------------------
#len(string)返回字符串长度
print(len(str))
#----------------------------------------------------
#ljust(width[, fillchar])返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
print("abc".ljust(20,"*"))#abc*****************
print("abc".rjust(20,"*"))#*****************abc
#----------------------------------------------------
#lower()转换字符串中所有大写字符为小写.
print('ABC'.lower())
print('aBC'.lower())
#----------------------------------------------------
#lstrip()截掉字符串左边的空格或指定字符
print("     mmm".lstrip())
print("!!!abc".lstrip('!'))
#----------------------------------------------------
#maketrans(intab, outtab)创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
intab = "aeiou"
outtab="12345"
str = "this is string example....wow!!!"
trantab = str.maketrans(intab, outtab)
#把str中的aeiou等字符转化为12345
print(str.translate(trantab))#th3s 3s str3ng 2x1mpl2....w4w!!!
#----------------------------------------------------
#max(str)返回字符串 str 中最大的字母。
print(max("slkfj"))#s
print(min("lsdjta"))#a
#----------------------------------------------------
#replace(old, new [, max])把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
str = "www.w3cschool.cc"
print ("菜鸟教程旧地址：", str)
print ("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!!"
print (str.replace("is", "was", 1))#thwas is string example....wow!!!
#----------------------------------------------------
#str.rfind(str, beg=0 end=len(string))返回字符串最后一次出现的位置，如果没有匹配项则返回-1。类似于 find()函数，不过是从右边开始查找.
str1 = "this is really a string is example....wow!!!"
str2 = "is"
print (str1.rfind(str2))#24
print (str1.rfind(str2, 0, 10))#5
print (str1.rfind(str2, 10))#24
print (str1.rfind(str2, 10,0))#-1
#----------------------------------------------------
#rindex( str, beg=0, end=len(string))类似于 index()，不过是从右边开始.
print (str1.rindex(str2))#24
print (str1.rindex(str2, 0, 10))#5
print (str1.rindex(str2, 10))#24
#----------------------------------------------------
#rjust(width,[, fillchar])返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
#----------------------------------------------------
#rstrip()删除字符串字符串末尾的空格.
#----------------------------------------------------
#split(str="", num=string.count(str)) num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
str = "this is string example....wow!!!"
print (str.split())#['this', 'is', 'string', 'example....wow!!!']
print (str.split('i',1))#['th', 's is string example....wow!!!']
print (str.split('w'))#['this is string example....', 'o', '!!!']
#----------------------------------------------------
#splitlines([keepends])按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print('ab c\n\nde fg\rkl\r\n'.splitlines())#['ab c', '', 'de fg', 'kl']
print('ab c\n\nde fg\rkl\r\n'.splitlines(True))
    #['ab c\n', '\n', 'de fg\r', 'kl\r\n']
#----------------------------------------------------
#startswith(str, beg=0,end=len(string))检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
print("!!!abc".startswith("!!!",0,10))
#----------------------------------------------------
#strip([chars])在字符串上执行 lstrip()和 rstrip() 移除字符串头尾指定的字符。
print("!!abc!".strip("!"))
#----------------------------------------------------
#swapcase()将字符串中大写转换为小写，小写转换为大写
print("AbcD".swapcase())
#----------------------------------------------------
#title()返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print("she is my love".title())
#----------------------------------------------------
#translate(table, deletechars="")根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
#table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
#deletechars -- 字符串中要过滤的字符列表。
# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))#b'RUNB'
#----------------------------------------------------
#upper()转换字符串中的小写字母为大写
#----------------------------------------------------
#zfill (width)返回长度为 width 的字符串，原字符串右对齐，前面填充0
str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))#str.zfill :  this is string example from runoob....wow!!!
print ("str.zfill : ",str.zfill(50))#str.zfill :  000000this is string example from runoob....wow!!!
#----------------------------------------------------
#str.isdecimal()如果字符串是否只包含十进制字符返回True，否则返回False。
str = "runoob2016"
print (str.isdecimal())#False
str = "23443434"
print (str.isdecimal())#True
