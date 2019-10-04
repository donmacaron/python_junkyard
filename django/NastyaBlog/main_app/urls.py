from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.post_list, name='index'),
    path('logout/',views.log_out, name='logout')
]
