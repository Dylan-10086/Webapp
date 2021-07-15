"""为 app users 建立 URL pattern"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # 包含默认身份验证的 URL
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]
