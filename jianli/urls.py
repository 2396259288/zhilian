from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.create_jianli, name = 'create_jianli'),
    path('pro_exper', views.pro_exper, name = 'pro_exper'),
    path('work_exper', views.work_exper, name = 'work_exper'),
    path('show_jianli', views.show_jianli, name = 'show_jianli'),
    path('push_jianli1', views.push_jianli1, name = 'push_jianli1'),
    path('push_jianli', views.push_jianli, name = 'push_jianli'),
    path('upload_jianli', views.upload_jianli, name = 'upload_jianli'),

]
