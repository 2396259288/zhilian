from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.indexView, name = 'index'),
    path('sort/', views.sort, name = 'sort'),
    # path('click/', views.click, name = 'click'),
    path('info/', views.info, name = 'info'),
    path('tongji/', views.tongji, name = 'tongji'),

]
