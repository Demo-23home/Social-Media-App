from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
    'author': 'Demo',
    'title': 'Blog Post1',
    'content':'First Post Content',
    'date_posted':'Augest 26,2018'
    },
     {
    'author': 'Zeyad',
    'title': 'Blog Post2',
    'content':'Second Post Content',
    'date_posted':'October 3,2019'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})