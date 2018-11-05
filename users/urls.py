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
    url(r'^form$',form),

    # json数据获取
    url(r'^json_data$',json_data),

    # 请求头数据
    url(r'^headers$',headers),

    # 其他请求对象
    url(r'^other$',other)

]
