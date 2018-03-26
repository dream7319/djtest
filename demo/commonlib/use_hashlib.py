#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_hashlib.py
@time: 2018/3/26 15:45
'''
__author__ = 'lierl'

#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等

import hashlib
md5 = hashlib.md5()
md5.update('how do you do '.encode('utf-8'))
md5.update('do'.encode('utf-8'))
print(md5.hexdigest())

md6 = hashlib.md5()
md6.update('how do you do do'.encode('utf-8'))
print(md6.hexdigest())

#以上二者的md5值是一样的

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
#比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长


def login(username, password):
    db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }

    try:
        dbpwd = db[username]
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        userpwd = md5.hexdigest()
        if dbpwd == userpwd:
            return True
        else:
            return False
    except KeyError as e:
        return False

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
import random
print(''.join([chr(random.randint(48, 122)) for i in range(20)]))
print(chr(110))