from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from post_app.models import Post


# Create your views here.
# o Padrão MVC em Django 

# M = models
# V = Views
# C = controlers

#falando em arquivos seria equivalente a:
# MVC     MTV
#  M   =   M  =  models.py
#  V   =   T  =  template
#  C   =   V  =  viewes.py




def home(request):
    return HttpResponse("ola mundo")


def allPosts(request):
    return HttpResponse(f'Post a seguir: {Post.postManager.all()}')