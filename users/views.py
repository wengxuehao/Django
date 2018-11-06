import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View


def index(request):  # 必须接收resquest参数，封装了客户端的请求信息
    # 必须返回一个HttpResponse对象
    # raise Exception('test')
    return HttpResponse('OKhehehe')


def hello_world(request):
    # path = reverse('hello')
    # 在工程urls.py里面使用了namespace的，就等于是加了前缀，需要在反向解析时候加上这个前缀
    path = reverse('users:hello')
    print(path)
    return HttpResponse('hello world')


def hello_world2(request):
    return HttpResponse('hello world 2')


def hello_world3(request):
    return HttpResponse('hello world 3')


# Http

# 请求行
# 请求头
# 请求体

# 请求数据的获取
# flask--
# request.json
# request.args
# request.form
# request.files


def weather(request, city, year):
    # 在url中定义了几个分组，那么这里就接收几个参数，
    # 参数传递的顺序和分组顺序传递
    print("城市：　", city)
    print("年份：　", year)
    return HttpResponse('OK')


def weather_named(request, year, city):
    # 命名的形式，参数传递顺序不按照分组顺序传递，只按照名字来
    print('城市：  ', city)
    print('年份是： ', year)
    return HttpResponse('OK')


# 查询字符串
def query_params(request):
    # 获取查询字符串
    args = request.GET
    # 获取最后一个值
    print(args.get('a'))
    print(args.get('b'))
    # 获取a里面的所有的值
    print(args.getlist('a'))

    print(args)

    return HttpResponse('OK')


# post请求体
def form(request):
    form_data = request.POST
    print(form_data)
    print(form_data.get('a'))
    print(form_data.getlist('a'))
    print(form_data.get('b'))
    # 不论客户端的请求方式是什么，request.GET一定可以拿到查询字符串的数据
    args = request.GET
    print(args)

    return HttpResponse('OK')


# json数据获取
def json_data(request):
    # 拿到原始数据
    body = request.body
    # 解码bytes
    body_str = body.decode()
    # 数据类型转换
    json_str = json.loads(body_str)
    print(json_str)
    return HttpResponse('OK')


# 请求头]
def headers(request):
    data = request.META
    print(data.get('CONTENT_TYPE', 'none'))
    return HttpResponse('OK')


# 其他请求对象
def other(request):
    print('method', request.method)
    print('user', request.user)
    print('path', request.path)
    print('encoding', request.encoding)
    print('files', request.FILES)
    return HttpResponse('OK')


# 响应
# HttpResponse响应
def create_HttpResponse(resquest):
    # 自定义响应头的内容，类字典对象
    response = HttpResponse('create_HttpResponse 1', content_type='text/html', status=201, reason='success')
    # 设置额外的响应头
    response['test_header'] = 'test'
    return response


# 自己创建json响应
def create_json_response(request):
    # data = {
    #     "a": 100,
    #     "b": 190,
    # }

    data_list = [1, 2, 3, 4, 5]
    # 把字典转换成json字符串
    # data_str = json.dumps(data)
    # response = HttpResponse(data_str, content_type='application/json')

    # 使用JsonResponse
    # response = JsonResponse(data)

    # 返回非字典数据对象
    response = JsonResponse(data_list, safe=False)
    return response


# 重定向
def create_redirect(request):
    # redirect重定向到绝对路径，需要加前缀
    return redirect('/users/hello/')


# 设置cookie
def create_cookie(request):
    response = HttpResponse('create cookie')
    # 设置cookie,在响应里面设置set_cookie
    response.set_cookie('test_key', "test_value")

    response.set_cookie('test_key_with_max_age', "test_value_with_max_age", max_age=60 * 60)

    return response


# 读取客户端的cookie

def read_cookie(request):
    # 从请求对象读取COOKIES
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse('read_cookie')


# 保存session数据
def save_session(request):
    session = request.session
    # 保存key:value
    # 不同的客户端保存不同的session数据
    session['test'] = 'test_value'
    return HttpResponse('save_session')


# 读取session数据
def read_session(request):
    session = request.session
    print(session.get('test', 'none'))
    return HttpResponse('read session')


# 删除session数据
def del_session(request):
    session = request.session
    # if 'test' in session:
    #     del session['test']

    # clear 删除session中保存的值
    # session.clear()
    # flush删除掉整个session
    session.flush()
    return HttpResponse('del session')


# 设置过期时间
def session_set_expiry(request):
    session = request.session
    session.set_expiry(5)
    return HttpResponse('set_expiry')


# 类视图
# GET 数据查询
# POST 数据创建
# PUT 数据更新
# DELETE 数据删除

# 针对类视图-定义带有self的装饰器
# def my_decorator(func):
#     def wrapper(self, request, *args, **kwargs):
#         print('请求的路径是：　', request.path)
#         return func(self, request, *args, **kwargs)
#
#     return wrapper


# 针对函数视图-定义不带self的装饰器2
def my_decorator2(func):
    def wrapper(request, *args, **kwargs):
        print('请求的路径是：　', request.path)
        return func(request, *args, **kwargs)

    return wrapper


# 定义万能的装饰器，不加self
# 只需要在相应的类视图函数上面加上method_decorator()
# 这样会自动加上self
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('请求的路径是：　', request.path)
        return func(request, *args, **kwargs)

    return wrapper


# 函数的形式定义的视图函数
@my_decorator2
def user(request):
    method = request.method
    if method == 'GET':
        return HttpResponse('get')


# １可读性好
# ２代码可复用
# @method_decorator(my_decorator, name='get')
# name 只是表名装饰的方法是哪一个
@method_decorator(my_decorator, name='dispatch')
class UserView(View):
    def get_name(self):
        return '小明'

    def get(self, request):
        # 查找姓名
        self.get_name()
        return HttpResponse('get')

    # 在对应的方法上面进行装饰method_decorator()自动加上self
    # @method_decorator(my_decorator)
    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        # 查找姓名
        self.get_name()
        return HttpResponse('put')

    def delete(self, request):
        # 查找姓名
        self.get_name()
        return HttpResponse('delete')


# 类扩展

class CreateMixin(object):
    def create(self):
        print('调用create')
        return 'create'


class UpdateMixin(object):
    def update(self):
        print('调用update')
        return 'update'


class DropMixin(object):
    def drop(self):
        print('调用delete')
        return 'delete'


# 继承父类，子类继承拥有父类的方法，等于就是子类扩展了，代码复用－－扩展类
class BookView(CreateMixin, UpdateMixin, DropMixin, View):
    # def create(self):
    #     print("创建")

    def post(self, request):
        print('创建数据')
        self.create()
        return HttpResponse('post')

    def put(self, request):
        print('更新数据')
        self.update()
        return HttpResponse('put')

    def delete(self, request):
        print('删除数据')
        return HttpResponse('delete')


class GoodsView(CreateMixin, UpdateMixin, View):
    # def create(self):
    #     print("创建")

    def post(self, request):
        print('创建数据')
        self.create()
        return HttpResponse('post')

    def put(self, request):
        print('更新数据')
        return HttpResponse('put')

    def delete(self, request):
        print('删除数据')
        return HttpResponse('delete')


# 模板的基本使用
def index1(request):
    # 1.获取模板
    # template=loader.get_template('index.html')
    context = {'city': "北京",
               'adict': {
                   'name': '⻄游记',
                   'author': '吴承恩'
               },
               'alist': [1, 2, 3, 4, 5]
               }
    # return HttpResponse(template.render(context))

    # 1. 找到模板 loader.get_template(模板⽂件在模板⽬录中的相对路径) -> 返回模板对象
    # 2. 渲染模板 模板对象.render(context=None, request=None) -> 返回渲染后的html⽂本字符串 context 为模板变量字
    # 典， 默认值为None request 为请求对象， 默认值为None
    return render(request, 'index.html', context)
