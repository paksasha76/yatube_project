from django.shortcuts import render
def index(request):    
    return render('Главная страница')
def group_posts(request, slug):
    return render(f'Группы {slug}')
# Create your views here.
