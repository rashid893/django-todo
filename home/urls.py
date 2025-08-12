from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("toggle/<int:task_id>/", views.toggle, name="toggle"),
    path("delete/<int:task_id>/", views.delete, name="delete"),
]