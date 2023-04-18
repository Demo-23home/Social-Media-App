from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
# from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
# posts=[
#     {
#     'author': 'Demo',
#     'title': 'Blog Post1',
#     'content':'First Post Content',
#     'date_posted':'Augest 26,2018'
#     },
#      {
#     'author': 'Zeyad',
#     'title': 'Blog Post2',
#     'content':'Second Post Content',
#     'date_posted':'October 3,2019'
#     }
# ]


def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']   #>>'date_posted'>>oldest to newest , add '-' to reverse


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']



    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        



def about(request):
    return render(request, 'blog/about.html',{'title':'About'})