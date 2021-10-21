from django.shortcuts import render
def index(request):    
    return render('Главная страница')
def group_posts(request):
    return render('Группы')
# Create your views here.
