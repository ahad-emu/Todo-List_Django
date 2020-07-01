from django.urls import path
from TodoList_App import views


urlpatterns = [
    path("", views.home, name ='home'),
    path("home/", views.show_list, name='show_list'),
    path("about/", views.about, name='about'),
    path("insert_item/", views.insert_item, name ='insert_item'),
    path("insert/", views.insert, name ='insert'),
    path("delete/<list_id>", views.delete, name='delete'),
    path("edit/<list_id>", views.edit, name="edit"),
]
