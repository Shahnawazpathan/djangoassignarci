from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('book_crud/', views.book_crud, name='book_crud'),
    path('book_update_delete/<int:pk>/', views.book_update_delete, name='book_update_delete'),
    path('search_book/', views.search_book, name='search_book'),

]
