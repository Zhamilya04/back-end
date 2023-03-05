from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.home_page),
    path('api/todo-lists', views.category_page),
    path('about', views.about_page),
    path('api/todo-lists', views.todolist_handler),
    path('api/todo-lists/:id', views.todolist_handler),
    path('api/todo-lists/:id/todos', views.todolist_todo_handler),
    path('api/todos', views.todo_handler),
    path('api/todos/:id', views.todo_handler)
]
