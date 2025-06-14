from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compress/', views.compress_image, name='compress_image'),
] 