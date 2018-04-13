1、当连接mysql数据库时会出现mysqldb的问题，需要在__init__中添加pymysql
2、python manage.py makemigrations 为修改之后的模型创建迁移文件，polls/migrations/0001.initial.py
3、python manage.py migrate 将这些改变更新到数据库
4、python manage.py check 检查项目中模型是否存在问题
5、python manage.py sqlmigrate polls 0001 根据迁移文件名返回sql语句
6、python manage.py createsuperuser
    创建能够登录管理站点的用户
    http://localhost:8002/admin/

7、创建项目依赖文件：pip freeze  > ./requirements.txt
8、导入第三方依赖库：pip install -r requirements.txt

用于WEB开发的Django/Flask，
用于科学计算的 Numpy/Scipy，
用于机器学习的 Scikit-Learn，
用于运维的 Supervisor/Fabric，
用于网络爬虫的 BeautifulSoup/Scrapy









