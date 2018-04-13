#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_括号匹配.py
@time: 2018/4/13 16:45
'''
__author__ = 'lierl'


'''
给定一个字符串，里边可能包含“()”、"{}"、“[]”三种括号，请编写程序检查该字符串的括号是否成对出现。
输出：
true：代表括号成对出现并且嵌套正确，或字符串无括号字符。
false：未正确使用括号字符。

实现思路：
使用list来代替栈实现相同的操作。声明了几个变量：

1、BRANKETS：由配对的括号组成的字典，注意使用右括号作为key，因为我们要判断的是右括号是否与左括号匹配，在字典中找出与key对应的value简单，要是找value对应的key要复杂一些。
2、BRANKETS_LEFT与BRANKETS_RIGHT分别存放左括号与右括号，用来判断字符属于哪个阵营。
'''

BRANKETS = {'}':'{',']':'[',')':'('}
BRANKETS_LEFT  = BRANKETS.values()
BRANKETS_RIGHT = BRANKETS.keys()

def bracket_check(string):
    #括号匹配检测
    stack = []
    for char in string:#遍历字符串
        #判断是否是左括号
        if char in BRANKETS_LEFT:
            #入栈
            stack.append(char)

        elif char in BRANKETS_RIGHT:
            if stack and stack[-1] == BRANKETS[char]:
                print(stack)
                stack.pop()#出栈
            else:
                return False
    return not stack

def main():
    print(bracket_check('{brace*&^[square(round)]end}'))
    print(bracket_check('{brace*&^[square(round])end}'))

main()