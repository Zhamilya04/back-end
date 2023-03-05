from django.urls import path
from students import views

urlpatterns = [
    path('/api/students', views.handle_categories),
    path('/api/students/:id', views.handle_category),

]
