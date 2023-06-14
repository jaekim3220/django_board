from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test

# # Create your views here.

# home 화면을 구성하는 html생성, requests는 templates 까지 생략
def home(requests):
    return render(requests, 'home.html')

# urls.py의 path('authors', views.author_list),
def author_list(requests):
    return render(requests, 'author/author_list.html')

# urls.py의 path('authors', views.author_list),
def post_list(requests):
    return render(requests, 'post/post_list.html')