#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: use_hmac.py
@time: 2018/3/26 16:19
'''
__author__ = 'lierl'

import hmac

message = b'hello world'
key = b'secret'
h = hmac.new(key, message, digestmod='md5').hexdigest()
print(h)

print('aa'.encode(encoding='utf-8', errors='ignore'))

import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

def login(username, password):
    db = {
        'michael': User('michael', '123456'),
        'bob': User('bob', 'abc999'),
        'alice': User('alice', 'alice2008')
    }
    try:
        user = db[username]
        return user.password == hmac_md5(user.key, password)
    except KeyError as e:
        return False

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')