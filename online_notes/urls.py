"""定义online_notes的url模式"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$',views.index,name='index'),

    # 显示所有的主题
    url(r'^topics/$',views.topics,name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    # 添加主题
    url(r'^new_topic/$',views.new_topic,name='new_topic'),

    # 用于添加新条目的界面
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
]
