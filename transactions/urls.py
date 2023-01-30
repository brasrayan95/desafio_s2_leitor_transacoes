from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_file, name="get_file"),
    path("transactions/", views.show_trans, name="show_trans"),
]
