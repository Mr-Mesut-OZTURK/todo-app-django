from django.urls import path
from .views import home, todo_list, todo_add, todo_update, todo_delete

urlpatterns = [
    path('', home, name='home'),
    path('list', todo_list, name='list'),
    path('add', todo_add, name='add'),
    path('update/<int:id>/', todo_update, name='update'),
    path('delete/<int:id>/', todo_delete, name='delete'),
]