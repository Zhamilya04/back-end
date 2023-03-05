from django.urls import path
from todo_app import views

urlpatterns = [
    path('api/todo-lists', views.todo_list_handler),
    #path('api/todo-lists/:id', views.category_handler),
    #path('api/todo-lists/:id/todos', views.category_products_handler),
    #path('api/todos', views.products_handler),
    #path('api/todos/:id', views.product_handler)
]