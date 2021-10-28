from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    template = 'posts/index.html' 
    title = "Это главная страница ютуб"
    context = {
        'title': title,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'text': text,
    }
    return render(request, {slug}, template, context)
# Create your views here.
