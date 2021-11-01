from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Post, Group

def index(request):
    title = 'Главная страница ютуб'
    text = 'Здесь будет главная страница ютуб'
    template = 'posts/index.html' 
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': title, 
        'text': text,
    }
    return render(request, template, context)

def group_posts(request, slug):
    title = 'Главная страница ютуб'
    text = 'Здесь будет главная страница ютуб'
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title, 
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
# Create your views here.
