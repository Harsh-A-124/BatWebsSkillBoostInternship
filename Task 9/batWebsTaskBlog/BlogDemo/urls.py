"""
URL configuration for batWebsTaskBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView,PostDetailsView,AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikePostView,AddCommentView, LandingView, UpvoteCommentView, DownvoteCommentView
# from .views import UpdateCategoryView
urlpatterns = [
    path('',LandingView,name="home"),
    path('<int:pi>',HomeView.as_view(),name="home-final"),
    path('postdetails/<int:pk>',PostDetailsView.as_view(),name="post-details"),
    path('addpost/',AddPostView.as_view(),name="add-post"),
    path('addcategory/',AddCategoryView.as_view(),name="add-category"),
    path('updatepost/<int:pk>',UpdatePostView.as_view(),name="update-post"),
    # path('updatecategory/<int:pk>',UpdateCategoryView.as_view(),name="update-category"),
    path('deletepost/<int:pk>',DeletePostView.as_view(),name="delete-post"),
    path('category/<str:cat>/',CategoryView,name="category"),
    path('categories/',CategoryListView,name="categories"),
    path('likepost/<int:pk>',LikePostView,name="like-post"),
    path('postdetails/<int:pk>/addcomment/',AddCommentView.as_view(),name="add-comment"),
    path('upvotecomment/<int:pk>',UpvoteCommentView,name="upvote-comment"),
    path('downvotecomment/<int:pk>',DownvoteCommentView,name="downvote-comment"),
]
