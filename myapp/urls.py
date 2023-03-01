from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("hello/<int:id>", views.hello_world),
    path("about/", views.about),
]
