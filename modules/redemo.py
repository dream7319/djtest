import re

def redemo1():
    print(re.match("www","www.baidu.com").span())# 在起始位置匹配
    print(re.match("www","www.baidu.com")) # 不在起始位置匹配

def demo2():
    line = "Cats are smarter than dogs"
    matchObj = re.match(r"(.*) are (.*?).*",line,re.M|re.I)
    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
# redemo1()
demo2()
