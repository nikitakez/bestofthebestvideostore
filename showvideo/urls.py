from django.urls import  re_path
from . import  views




urlpatterns = [
    re_path("123/", views.hello),
    re_path("456/", views.world)
]