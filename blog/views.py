from django.shortcuts import render
from django.contrib import admin

def post_list(request):
    return render(request, 'blog/post_list.html')
