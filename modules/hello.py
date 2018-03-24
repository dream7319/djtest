#!/usr/bin/env python3          此行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-         表示.py文件本身使用标准UTF-8编码；
'''
 test module        模块的文档注释 任何模块代码的第一个字符串都被视为模块的文档注释
'''
__author__ = 'lierl'#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys

def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello, %s" %args[1])
    else:
        print("too many arguments")

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__ == '__main__':
    test()