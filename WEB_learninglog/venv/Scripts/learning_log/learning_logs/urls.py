# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     # 主页
#     url(r'^$', views.index, name='index'),
# ]
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]