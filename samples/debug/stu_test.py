#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: stu_test.py
@time: 2018/3/25 8:38
'''
__author__ = 'lierl'

from samples.debug.myStu import Student
import unittest
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()

# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
#
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
#
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
#
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。