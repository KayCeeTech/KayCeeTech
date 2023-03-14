from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name="Hello"),
    path('greet', views.greet, name="greet"),
    path('come', views.come, name="come"),
    path('creat', views.creat, name="creat"),
]
