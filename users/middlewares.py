# 中间件
def simple_middleware(get_response):
    print('django 初始化时执行的代码1')

    def middleware(request):
        print('视图函数调用之前执行的代码1')
        # flask中是独立定义的一个函数

        response = get_response(request)  # 相当于调用视图函数

        print('视图函数调用之后执行的代码1')
        # flask中是独立定义的一个函数
        return response

    return middleware


# 中间件
def simple_middleware2(get_response):
    print('django 初始化时执行的代码2')

    def middleware(request):
        print('视图函数调用之前执行的代码2')
        # flask中是独立定义的一个函数

        response = get_response(request)  # 相当于调用视图函数

        print('视图函数调用之后执行的代码2')
        # flask中是独立定义的一个函数
        return response

    return middleware


# 中间件
def simple_middleware3(get_response):
    print('django 初始化时执行的代码3')

    def middleware(request):
        print('视图函数调用之前执行的代码3')
        # flask中是独立定义的一个函数

        response = get_response(request)  # 相当于调用视图函数

        print('视图函数调用之后执行的代码3')
        # flask中是独立定义的一个函数
        return response

    return middleware

