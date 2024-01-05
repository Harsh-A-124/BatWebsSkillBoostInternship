from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import AddPostForm,UpdatePostForm,AddCommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import LoginView
import math

def LandingView(request):
    return redirect('home-final',pi=1)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        limit = self.kwargs['pi'] * 10
        start = limit - 10
        return queryset.all()[start:limit]
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        pi = self.kwargs['pi']
        prev = pi-1
        next = pi+1
        limit = self.kwargs['pi'] * 10
        start = limit - 10
        qs_count = super().get_queryset().count()
        page_count = math.ceil(qs_count/10)
        page_range = range(1,page_count+1)
        context["cat_menu"] = cat_menu
        context["pi"] = pi
        context["start"] = start
        context["limit"] = limit
        context["qs_count"] = qs_count
        context["page_count"] = page_count
        context["page_range"] = page_range
        context["prev"] = prev
        context["next"] = next
        return context

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(PostDetailsView,self).get_context_data(*args,**kwargs)
        post_info = get_object_or_404(Post,id=self.kwargs['pk'])
        like_count = post_info.total_likes()
        if post_info.likes.filter(id=self.request.user.id).exists():
            liked = True
        else:
            liked = False
            
        comment_dict = {}
        post_comments = Comment.objects.filter(post=post_info)
        for comment in post_comments:
            comment_upvotes = comment.total_upvotes()
            comment_downvotes = comment.total_downvotes()
            comment_dict[comment]={'upvoted':None,'downvoted':None,'upvotes':comment_upvotes, 'downvotes':comment_downvotes}

        context["cat_menu"] = cat_menu
        context["like_count"] = like_count
        context["liked"] = liked
        context["comment_dict"] = comment_dict
        return context

class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')
    success_url = reverse_lazy('home')
    success_message = "Post added successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    success_message = "Category added successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(AddCategoryView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(SuccessMessageMixin,UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    # fields = ('title','title_tag','body')
    success_url = reverse_lazy('home')
    success_message = "Post updated successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(UpdatePostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

# class UpdateCategoryView(UpdateView):
#     model = Category
#     template_name = 'update_category.html'
#     fields = '__all__'

class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Post deleted successfully!"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.filter(id__lte=5)
        context = super(DeletePostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cat):
    cat_menu = Category.objects.filter(id__lte=5)
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))
    return render(request,'category.html',{'cat':cat.title().replace('-', ' '),'category_posts':category_posts,'cat_menu':cat_menu})

def CategoryListView(request):
    cat_menu = Category.objects.filter(id__lte=5)
    category_menu_list = Category.objects.all()
    return render(request,'categories.html',{'category_menu_list':category_menu_list,'cat_menu':cat_menu})

def LikePostView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('postid'))
    # liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        # liked = False
    else:
        post.likes.add(request.user)
        # liked = True
    return HttpResponseRedirect(reverse('post-details',args=[str(pk)]))

class AddCommentView(SuccessMessageMixin,CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    # fields = ('title','body')
    # success_url = reverse_lazy('home')
    success_message = "Comment posted successfully!"

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.filter(id__lte=5)
    #     context = super(AddCommentView,self).get_context_data(*args,**kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context

    def get_context_data(self, *args, **kwargs):
        postpk = self.kwargs['pk']
        user = self.request.user
        context = super(AddCommentView,self).get_context_data(*args,**kwargs)
        context["postpk"] = postpk
        context["user"] = user
        return context
    
def UpvoteCommentView(request,pk):
    comment = get_object_or_404(Comment, id=request.POST.get('commentid'))
    # upvoted = False
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
        # upvoted = False
    else:
        comment.upvotes.add(request.user)
        # upvoted = True
    return HttpResponseRedirect(reverse('post-details',args=[str(pk)]))

def DownvoteCommentView(request,pk):
    comment = get_object_or_404(Comment, id=request.POST.get('commentid'))
    # downvoted = False
    if comment.downvotes.filter(id=request.user.id).exists():
        comment.downvotes.remove(request.user)
        # downvoted = False
    else:
        comment.downvotes.add(request.user)
        # downvoted = True
    return HttpResponseRedirect(reverse('post-details',args=[str(pk)]))