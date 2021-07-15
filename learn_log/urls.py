"""定义 learn_log 的 URL 模式"""  # 文档字符串，用于指出该 urls.py 文件位于哪个 app 中

from django.urls import path  # 使用 path 将 URL 映射到视图中

from . import views

app_name = 'learn_log'  # 用于与其他 urls.py 文件区分开

"""
    path函数的三个实参:
        1.是个字符串，帮助 Django 正确的 route 请求。请求时，会搜索所有的 URL pattern ，
        找到匹配的那个。Django 会忽略基础 URL(http://localhost:8000/), 故''(空字符串)会与基础 URL 匹配
        2.指定调用 views.py 文件中的函数，若 URL 与 1. 中表达式匹配，则会调用 views 中的 index() 函数
        3.将该 URL pattern 命名为 'index' 便于其他地方引用
"""
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 显示特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用于修改特点条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]
