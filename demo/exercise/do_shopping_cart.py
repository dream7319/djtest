#!/usr/bin/env python3
# encoding:utf-8
'''
@author: lierl
@file: do_shopping_cart.py
@time: 2018/3/31 11:44
'''
import datetime

__author__ = 'lierl'

'''
程序要求

1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录

shopping过程中余额不足的话，无法在购物过程中直接充值，所以增加了判断，让用户在购物过程中可以选择充值、退出、返回

循环打印第一级的分类的时候，使用enumerate，可以输出下标，而脚本中没有使用下标进行判断，而是让用户直接输入分类名称，实际上这个地方使用enumerate更灵活，后面判断用户输入的时候，可以用下标判断或用分类判断
开始使用了os.system('clear')，但是发生乱码问题，应该是字符集的问题
'''
import json
import re
import hashlib
'''
编码：把一个Python对象编码转换成Json字符串   json.dumps()   返回str
解码：把Json格式字符串解码转换成Python对象   json.loads()   返回dict,也可转为相应的对象

问题：
为何不把加载database.json之后的数据声明成全局变量,因为个人可能多次购买，每购买一次会写入到database.json,如果生命全局变量，则加载新的数据，会导致问题
'''

welcome_info = '''
1. 按"A"注册
2. 按"B"登录
3. 按"Q"退出
'''

#加载json文件,默认加载database.json
def _load_database(filename = 'database.json'):
    with open(file=filename, mode='r', encoding='utf-8') as f:
        database = json.load(f)
    return database#dict字段

#用于将购物相关信息保存到JSON文件，比如购物时间，购物历史，购物列表，账户余额，创建的新用户和现有已存在用户信息
def _save_account(database, filename='database.json'):
    # 打开并可写文件,若文件已存在，则以前的内容将被清除
    with open(file=filename, mode='w', encoding="utf-8") as f:
        json.dump(database, f, indent=4, sort_keys=True, ensure_ascii=False)#把dict写入到文件中

#获取当前格式化后的时间
def _get_current_format_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#获取当前时间


#获取用户的购物日期
def _get_shopping_date(account):
    database = _load_database()
    return database[account]['shopping_time']

#获取历史购物信息
def _get_shopping_history(account):
    database = _load_database()
    account_data = database[account]#dict
    history_shopping_list = account_data['shopping_list']#list
    if len(history_shopping_list) > 0:#如果购物列表中有数据
        for history_shopping_data in history_shopping_list:
            buy_time = history_shopping_data['buy_time']#购买时间
            goods_name = history_shopping_data['goods_name']#商品名称
            goods_num = history_shopping_data['goods_num']#购买数量
            print("您于%s购买了%s件%s" % (buy_time, goods_num, goods_name))
    else:
        print("您的购物车是空的。。。")

#默认设置变量account=None来判断账号是否已经登录,如果没有登录就退出,则不打印购物信息
#如果已经登录过,则打印购物历史信息
def _logout(account_name = None):
    if account_name is not None:
        _get_shopping_history(account_name)
    print('感谢您的光临,欢迎下次光临')
    exit()

#获取账户余额
def _get_balance(account_name):
    database = _load_database()
    return database[account_name]['balance']

#购物
def _shopping(account_name):
    goods = _load_database(filename='goods.json')#从文件中获取所有的商品

    while True:
        goods_first = {}
        goods_first_index = []
        for index, good in enumerate(goods, start=1):
            goods_first[index] = good
            goods_first_index.append(index)
            print('商品编号:%s          商品类型：%s' % (index, good))
        shopping_first_no = input("请输入商品类型编号(按b返回上一页,按q退出)：").strip()
        if shopping_first_no.isdigit():
            shopping_first_no = int(shopping_first_no)
            if shopping_first_no in goods_first_index:
                while True:
                    goods_name = goods_first[shopping_first_no]
                    print("%s下有以下商品：" % goods_name)
                    goods_seconds = {}
                    goods_seconds_index = []
                    for index,good in enumerate(goods[goods_name].keys(), start=1):
                        print('商品编号:%s          商品名称：%s' % (index, good))
                        goods_seconds_index.append(index)
                        goods_seconds[index] = good

                    shopping_second_no = input("请输入商品名称编号(按b返回上一页,按q退出)：").strip()

                    if shopping_second_no.isdigit():
                        shopping_second_no = int(shopping_second_no)
                        if shopping_second_no in goods_seconds_index:
                            while True:
                                goods_third_name = goods_seconds[shopping_second_no]
                                print("有以下几种%s" % goods_third_name)
                                final_goods_name = goods[goods_name][goods_third_name]
                                goods_final = {}
                                goods_final_index=[]

                                for index, good in enumerate(final_goods_name.keys(), start=1):
                                    print('%s编号:%s          %s名称：%s          价格为:%s' % (goods_third_name, index, goods_third_name, good,final_goods_name[good]))
                                    goods_final[index] = good
                                    goods_final_index.append(index)
                                goods_final_no = input("请输入购买%s的编号(按b返回上一页,按q退出):" % goods_third_name).strip()
                                if goods_final_no.isdigit():
                                    goods_final_no = int(goods_final_no)
                                    if goods_final_no in goods_final_index:
                                        final_name = goods_final[goods_final_no]
                                        buy_num = input("请输入购买%s数量：" % final_name).strip()
                                        if buy_num.isdigit():
                                            buy_num = int(buy_num)
                                            database = _load_database()
                                            account_balance = database[account_name]['balance']
                                            goods_price = final_goods_name[final_name]
                                            sum_amount = buy_num * goods_price
                                            if account_balance >= sum_amount:
                                                database[account_name]['balance'] = account_balance - sum_amount
                                                shopping_list_data = {}
                                                shopping_list_data['buy_time'] = _get_current_format_time()
                                                shopping_list_data['goods_name'] = final_name
                                                shopping_list_data['goods_num'] = buy_num
                                                database[account_name]['shopping_list'].append(shopping_list_data)
                                                d1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
                                                _save_account(database)#保存购物时间到数据库中,即：database.json
                                                #提示用户买了什么东西
                                                print("您于%s购买了%s件%s" % (d1, buy_num, final_name))
                                            else:
                                                print('您的账户余额不足，请您及时充值！')
                                            return None
                                        else:
                                            print("您输入有误，请重新输入")
                                    else:
                                        print("您输入有误，请重新输入")
                                elif goods_final_no == 'q':
                                    _logout(account_name)
                                elif goods_final_no == 'b':
                                    break
                                else:
                                    print("您输入有误，请重新输入")
                        else:
                            print("您输入有误，请重新输入")
                    elif shopping_second_no == 'q':
                        _logout(account_name)
                    elif shopping_second_no == 'b':
                        print("进入这里没有？")
                        break
                    else:
                        print("您输入有误，请重新输入")
            else:
                print("您输入有误，请重新输入")
        elif shopping_first_no == 'q':
            _logout(account_name)
        elif shopping_first_no == 'b':
            return
        else:
            print("您输入有误，请重新输入")

#充值操作
def _recharge(account_name):
    database = _load_database()
    print("您的账户当前余额为：%.2f " % _get_balance(account_name))
    while True:
        input_data = input("您正在进行充值...请输入充值金额(按b返回上一页,按q退出)：").strip()
        if re.match(pattern=r'^\d+.\d{1,2}$', string=input_data):
            #输入的金额必须为数字,充值完毕写入库中,退出当前循环
            if input_data.isdigit():#整数数字
                amount = int(input_data)
            else:#小数
                amount = float(input_data)
            database[account_name]['balance'] += amount
            _save_account(database)
            #获取到当前用户余额
            curr_balance = _get_balance(account_name)
            print('您已成功充值,您的余额为\033[32m%.2f\033[0m元' % curr_balance)
            break
        elif input_data == 'b':
            break
        elif input_data == 'q':
            _logout(account_name)
        else:
            print("您输入的有误，请重新输入金额")

#登录
def _login():
    account_name = input("请输入账号(按q退出系统)：").strip()
    if account_name == 'q':
        _logout()
    else:
        #加载黑名单
        black_data_list = _load_database('black_list.json')
        black_user_list = []#用来存放所有的黑名单用户名
        for black_user in black_data_list.keys():
            black_user_list.append(black_user)

        #如果用户不在黑名单中
        if account_name not in black_user_list:
            #不在黑名单，则去判断是否在已有账户列表中
            current_data_list = _load_database()
            current_user_list = []
            for current_user in current_data_list.keys():
                current_user_list.append(current_user)

            if account_name in current_user_list:
                loginTimes = 1#登录次数
                # 输入用户在数据库中
                current_user_passwd = current_data_list[account_name]['pwd']#获取当前用户的密码
                while loginTimes <= 3:
                    input_passwd = input("请输入密码：").strip()
                    if _get_md5(input_passwd) == current_user_passwd:
                        #登录成功，修改最新登录时间
                        last_login_time = current_data_list[account_name]['last_login_time']
                        if last_login_time is not None:
                            print("登录成功,上一次登录时间：%s" % last_login_time)
                        else:
                            print("登录成功,您可以购物啦")
                        current_data_list[account_name]['last_login_time'] = _get_current_format_time()
                        _save_account(current_data_list)
                        #密码正确
                        account_balance = current_data_list[account_name]['balance']#根据账户获取账户余额
                        #高亮 打印账户余额
                        print('您的账户余额是\033[32m%.2f\033[0m' % account_balance)
                        while True:
                            #让用户输入特定字母进入特定的菜单
                            print("*"*60)
                            print("您可以进行以下操作：")
                            print("h: 查询购物历史")
                            print("s: 开始购物")
                            print("t: 充值")
                            print("q: 退出")
                            print("*" * 20)
                            command = input("请输入操作指令:").strip()
                            if command == 'h':#查询历史购物
                                _get_shopping_history(account_name)
                            elif command == 't':#充值操作
                                _recharge(account_name)
                            elif command == 's':#清空购物车,把shopping_list和shopping_time清空
                                # _clear_shopping_cart(account_name)
                                _shopping(account_name)  # 开始购物
                            elif command == 'q':
                                _logout(account_name)
                            else:
                                # 如果用户的操作不符合上面所有的情况，则输出错误信息
                                print('输入有误，请检查后重新输入！')
                    else:
                        # 不成功提示用户有三次机会，如果三次都不成功，将锁定用户名
                        if loginTimes == 3:  # 三次不成功
                            print("对不起，你输入的次数过多，你的用户名已经被锁定，请联系管理员")
                            #保存用户到black_list.json中
                            black_data_list[account_name] = None
                            # black_data_list.setdefault(account_name)
                            #添加到黑名单列表
                            _save_account(database=black_data_list, filename='black_list.json')
                            _logout()#退出登录
                        else:
                            print("对不起，你输入的密码不对，你还有%s次机会" % (3 - loginTimes))
                            loginTimes += 1
            else:
                #输入用户不在数据库中
                print('账号不存在，请重试！或输入b返回上一层，输入q，退出购物程序！')
                print('-----------------------------------------------------')
        else:#该账户在黑名单中,则打印信息并退出
            print("您的账号已经被锁定，请联系管理员处理")
            _logout()#退出

def _get_md5(str):
    h1 = hashlib.md5()
    h1.update(str.encode('utf-8'))
    return h1.hexdigest()

#添加账户
def _add_user():
    while True:
        account_name = input("请输入账户：").strip()
        if account_name is not '':
            while True:
                account_pwd = input("请输入密码：").strip()
                if account_pwd is not '':
                    #初始化数据
                    database = _load_database()
                    account_data_dict = {}
                    account_data_dict['shopping_list'] = []
                    account_data_dict['pwd'] = _get_md5(account_pwd)
                    account_data_dict['balance'] = 0.0
                    account_data_dict['last_login_time'] = None
                    account_data_dict['register_time'] = _get_current_format_time()
                    database[account_name] =  account_data_dict
                    _save_account(database)
                    print("注册成功，请重新登录进行购物")
                    break
                else:
                    print("账户密码不能为空,请重新输入")
            break
        else:
            print("账户号不能为空,请重新输入")

def main():
    while True:
        #打印登录提示信息
        '''
        1. 按"A"注册
        2. 按"B"登录
        3. 按"Q"退出
        '''
        print("*"*60)
        print("欢迎光临购物系统".rjust(10, ' '))
        print("您可以进行如下操作：".rjust(12, ' '))
        print("A:注册".rjust(6,' '))
        print("B:登录".rjust(6,' '))
        print("Q:退出".rjust(6,' '))
        print("*"*60)
        command = input("  请输入选项：").strip()#用户输入指令
        command = command.upper()
        if command == 'A':#创建用户
            _add_user()
        elif command == 'B':#登录
            _login()
        elif command == 'Q':#退出登录
            _logout()
        else:#如果用户输入选项不存在则需要重新输入
            print("输入信息有误,请重新输入")


if __name__ == '__main__':
    main()











