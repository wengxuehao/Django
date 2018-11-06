from django.conf.urls import url

from users.views import *

# urlpatterns是被Django识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要url函数来构造
    # url(路径,视图)
    url(r'^index/$', index),
    url(r'^hello/', hello_world, name='hello'),
    url(r'^hello2/$', hello_world2),
    url(r'^hello3/$', hello_world3),

    # 获取请求数据

    # TODO 匿名分组
    url(r'^weather/(\w+)/(\d+)$', weather),

    # TODO 命名分组
    url(r'^weather_named/(?P<city>\w+)/(?P<year>\d+)$', weather_named),

    # TODO 查询字符串
    url(r'^query_params$', query_params),

    # 表单数据获取
    url(r'^form$', form),

    # json数据获取
    url(r'^json_data$', json_data),

    # 请求头数据
    url(r'^headers$', headers),

    # 其他请求对象
    url(r'^other$', other),

    # 响应对象
    url(r"^create_HttpResponse$", create_HttpResponse),

    # 手动创建json响应
    url(r'^create_json_response$', create_json_response),

    # 响应返回JsonResponse
    url(r'^JsonResponse$', JsonResponse),

    # 重定向
    url(r'^create_redirect$', create_redirect),

    # 设置cookie
    url(r'^create_cookie$', create_cookie),

    # 读取cookie
    url(r'^read_cookie$', read_cookie),

    # 保存session
    url(r'^save_session$', save_session),

    # 读取session
    url(r'^read_session$', read_session),

    # 删除session
    url(r'^del_session$', del_session),

    # 设置session过期时间
    url(r'^session_set_expiry$', session_set_expiry),

    # 类视图
    url(r'^user$', UserView.as_view()),

    # 类视图使用装饰器
    # url(r'^user$', my_decorator(UserView.as_view())),
    url(r'^index1$',index1)

]
