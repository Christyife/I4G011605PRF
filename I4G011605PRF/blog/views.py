from pdb import post_mortem
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from I4G011605PRF.blog.models import Post

# Create your views here.

class PostListView
model=Post

class PostCreateView
model=Post
fields="__all__"
success_url=reverse_lazy("blog:all")

class PostDetailView
model=Post

class PostUpdateView
model=Post
success_url=reverse_lazy("blog:all")

class PostDeleteView
model=Post
fields="__all__"
success_url=reverse_lazy("blog:all")