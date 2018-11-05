import json

from django.http import HttpResponse
from django.urls import reverse


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


# 请求头
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
