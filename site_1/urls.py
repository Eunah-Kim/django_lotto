from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # path('') : 127.0.0.1:8000/  로 이동
    # path('', views.index),
    # view.py안에 있는 index 연결하기
    path('hello/', views.hello, name='hello_main'),
    path('lotto/', views.index, name='index'),
    path('lotto/new', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]

# 기본 url 주소 ; path(''); 127.0.0.1:8000/
# path('url 주소', views.함수명)
# 해당 url에 대해 실행될 함수를 views.py에 입력함.


# urlpatterns = [
#     # 127.0.0.1:8000/admin/
#     path('admin/', admin.site.urls),
#     # path('') : 127.0.0.1:8000/  로 이동
#     path('', views.index),
#     # view.py안에 있는 index 연결하기
#     # user의 요청이 같이 떠다니고 있음
#     # 127.0.0.1:8000/hello로 이동
#     path('hello/',views.hello, name='hello_main'),
# ]
