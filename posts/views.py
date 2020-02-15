from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DeleteView
from .models import Post
from django.http import HttpResponseRedirect,HttpResponse



class HomePageView(ListView):
    model = Post
    template_name = 'posts/index.html'    
    context_object_name = 'all_objects_list'    #explicit name


class UserPostListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'    
    context_object_name = 'posts'    #explicit name

    def get_queryset(self):                                                             #only the current log in user's post will be displpayed    
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')


class PostCreateView(LoginRequiredMixin,CreateView):
    
    model = Post
    template_name = 'posts/posts_form.html'
    success_url = '/'
    fields = ['text']
    
    def form_valid(self,form):                                          #this method will set the current user equal to the author 
            form.instance.author = self.request.user
            return super().form_valid(form)
        

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = ('/')

    def Test_func(self):                                                    #prohibiting the current user to delete the other user's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    




    
    