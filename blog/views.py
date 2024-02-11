from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Khumbo',
        'title': 'Blog Post 1',
        'content': 'Coding got hands',
        'date_posted': '10 Feb, 2024'
    },
    {
        'author': 'Viktor',
        'title': 'Blog Post 2',
        'content': 'Deadass bro',
        'date_posted': '14 Feb, 2024'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

