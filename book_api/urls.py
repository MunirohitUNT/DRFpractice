from django.contrib import admin
from django.urls import path
from book_api.views import book_list, book_create, book

urlpatterns = [
    path('', book_create),
    path('list/', book_list),   # when enter list,book_list will be called,data will be returned stored in that function
    path('<int:pk>', book)

]