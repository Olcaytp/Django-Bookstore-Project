# basic_app/urls.py
from django.urls import path
from basic_app import views

app_name = 'basic_app'  # Namespacing the URLconf module

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('add_book/', views.add_book, name='add_book'), 
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
