'''
字典操作
'''
#-------------------------------------------------------------------------
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))#3
#str(dict)输出字典，以可打印的字符串表示。
print(str(dict))#{'Age': 7, 'Name': 'Runoob', 'Class': 'First'}
#--------------------------------方法-------------------------------------
#radiansdict.clear()删除字典内所有元素
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict.clear()
print(dict)#{}
#-------------------------------------------------------------------------
#radiansdict.copy()返回一个字典的浅复制
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print (dict2)#{'Class': 'First', 'Age': 7, 'Name': 'Runoob'}
dict1 =  {'user':'runoob','num':[1,2,3]}
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
print(dict2)#{'num': [1, 2, 3], 'user': 'runoob'}
print(dict3)#{'num': [1, 2, 3], 'user': 'runoob'}
#实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
#-------------------------------------------------------------------------
#radiansdict.fromkeys(seq[, value]))创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ('name', 'age', 'sex')
dict={}
dict = dict.fromkeys(seq)
print (str(dict))#{'sex': None, 'name': None, 'age': None}
dict = dict.fromkeys(seq, 10)
print (str(dict))#{'age': 10, 'sex': 10, 'name': 10}
#-------------------------------------------------------------------------
#radiansdict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict1.get('Name'))#Runoob
print(dict1.get('Baidu','Baidu'))#Baidu
#-------------------------------------------------------------------------
#key in dict如果键在字典dict里返回true，否则返回false
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print('Name' in dict1)#True
print('Runoob' in dict1)#False
#-------------------------------------------------------------------------
#radiansdict.items()以列表返回可遍历的(键, 值) 元组数组
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict.items())#dict_items([('Name', 'Runoob'), ('Class', 'First'), ('Age', 7)])
#-------------------------------------------------------------------------
#	radiansdict.keys()以列表返回一个字典所有的键
print(dict.keys())#dict_keys(['Age', 'Class', 'Name'])
print(dict.values())#dict_values(['First', 'Runoob', 7])
#-------------------------------------------------------------------------
#radiansdict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict = {'Name': 'Runoob', 'Age': 7}
print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))#7
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))#None
print ("新字典为：", dict)#新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
#-------------------------------------------------------------------------
#radiansdict.update(dict2)把字典dict2的键/值对更新到dict里
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("更新字典 dict : ", dict)# {'Sex': 'female', 'Age': 7, 'Name': 'Runoob'}
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Age': '8' }
dict.update(dict2)
print(dict)#{'Age': '8', 'Name': 'Runoob'}
#-------------------------------------------------------------------------
#pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)#菜鸟教程
print(site)#{'url': 'www.runoob.com', 'alexa': 10000}
pop_obj = site.pop("aa","bb")
print(pop_obj)#bb
#-------------------------------------------------------------------------
#popitem()随机返回并删除字典中的一对键和值(一般删除末尾对)。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)#('name', '菜鸟教程')
print(site)#{'url': 'www.runoob.com', 'alexa': 10000}
#-------------------------------------------------------------------------
cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for key in cities:
    print("当前地址："+key+",有哪些区：",end='\n')
    for val in cities[key]:
        print(val+",有哪些景区呢：",end='\n')
        for address in cities[key][val]:
            print(address,end=',')
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
