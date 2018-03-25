#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from samples.debug.mydict import Dict

class TestDict(unittest.TestCase):
    #setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print("setUp")

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print("tearDown")

if __name__ == '__main__':
    unittest.main()

