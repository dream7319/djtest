from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
from myapp.models import User
from myapp.utils import MD5
from myapp import forms
from myapp.apps import MyappConfig

def index(request):
    # type(request) <class 'django.core.handlers.wsgi.WSGIRequest'>
    return render(request=request, template_name="index.html")

'''
说明：
1、每个视图函数都至少接收一个参数，并且是第一位置参数，该参数封装了当前请求的所有数据；
2、通常将第一参数命名为request，当然也可以是别的；
3、request.method中封装了数据请求的方法，如果是“POST”（全大写），将执行if语句的内容，如果不是，直接返回最后的render()结果；
4、request.POST封装了所有POST请求中的数据，这是一个字典类型，可以通过get方法获取具体的值。
5、类似get('username')中的键‘username’是HTML模板中表单的input元素里‘name’属性定义的值。所以在编写form表单的时候一定不能忘记添加name属性。
6、利用print函数在开发环境中验证数据；
7、利用redirect方法，将页面重定向到index页。
'''
#不适用form接收参数
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        print(username, password)
        #判断用户密码不能为空
        if username and password:
            '''
            通过get('username', None)的调用方法，确保当数据请求中没有username键时不会抛出异常，而是返回一个我们指定的默认值None；
            通过if username and password:确保用户名和密码都不为空；
            通过strip()方法，将用户名前后无效的空格剪除；
            更多的数据验证需要根据实际情况增加，原则是以最低的信任度对待发送过来的数据。
            '''
            username = username.strip()
            try:
                user = User.objects.get(name = username)
            except:
                return render(request=request, template_name="login.html", context={"error": "用户名或密码不正确"})
            if user.password == password:
                return redirect("/%s/index/" % MyappConfig.name)#重定向到首页
    return render(request=request, template_name="login.html")

'''
说明：
1、对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据；
2、对于POST方法，接收表单数据，并验证；
3、使用表单类自带的is_valid()方法一步完成数据验证工作；
4、验证成功后可以从表单对象的cleaned_data数据字典中获取表单的具体值；
5、如果验证不通过，则返回一个包含先前数据的表单给前端页面，方便用户修改。也就是说，它会帮你保留先前填写的数据内容，而不是返回一个空表！
    另外，这里使用了一个小技巧，Python内置了一个locals()函数，它返回当前所有的本地变量字典，我们可以偷懒的将这作为render函数的数据字典参数值，就不用费劲去构造一个形如{'message':message, 'login_form':login_form}的字典了。这样做的好处当然是大大方便了我们，但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。
'''
def login(request):
    if request.session.get('is_login', None):
        #如果已经登录，则直接跳转到首页
        return redirect("/%s/index/" % MyappConfig.name)

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == MD5.get_md5(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect("/%s/index/" % MyappConfig.name)#重定向到首页
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
    login_form = forms.UserForm()
    return render(request=request, template_name="login.html", context=locals())

def register(request):
    #首先判断当前用户是否是登录状态，如果是登录状态跳转到首页
    if request.session.get('is_login', None):
        return redirect("/%s/index/" % MyappConfig.name)

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容"
        if register_form.is_valid():
            # other = register_form.cleaned_data['other']
            # print(other)
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 == password2:
                user = User.objects.filter(Q(name=username) | Q(email=email))
                if not user:
                    new_user = User.objects.create()
                    new_user.name = username
                    new_user.password = MD5.get_md5(password1)
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()
                    return redirect("/%s/login/" % MyappConfig.name)
                else:
                    message="用户已存在,请重新输入用户名"
            else:
                message = "用户名密码不一致"
    register_form = forms.RegisterForm()
    return render(request=request, template_name="register.html", context=locals())

def logout(request):
    if not request.session.get('is_login', None):
        #如果本来就未登录
        return redirect("/%s/login/" % MyappConfig.name)
    request.session.flush()#一次性将session中的所有内容全部清空，确保不留后患
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/%s/login/" % MyappConfig.name)