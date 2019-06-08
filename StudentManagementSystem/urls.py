"""StudentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'classes_list/$', views.classes_list),    # 班级列表
    url(r'add_classes/$', views.add_classes),    # 添加班级
    url(r'delete_classes/$', views.delete_classes),    # 删除班级
    url(r'edit_classes/$', views.edit_classes),    # 编辑班级
]
