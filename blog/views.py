from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title':'Home',
    }
    return render(request,'blog/home.html',context)


# a generic class based view is going to look for a tempalte with the naming convention
# <app>/<model>_<viewtype>.html

#list based view of home
class PostListView(LoginRequiredMixin,ListView):
    model = Post #which models is the view linked to
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #to arrange them newest to oldest

    def form_valid(self,form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
    

#detailed view for each post
class PostDetailView(DetailView):
    model = Post

#'create' view for each post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

#'update' view for each post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#'delete' view
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'blog/about.html',{'title':'About the Project'})

