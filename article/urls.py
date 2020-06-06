from django.urls import path
from . import views
from article.views import ListArticleView,DetailArticleView,CreateArticleView,UpdateArticleView,DeleteArticleView

urlpatterns=[
path("",ListArticleView.as_view(), name='blog home'),
path("about/",views.about, name='blog about'),
path("detail/<int:pk>/",DetailArticleView.as_view(), name='detail'),
path("create/",CreateArticleView.as_view(), name='create'),
path("detail/<int:pk>/update/",UpdateArticleView.as_view(), name='update'),
path("detail/<int:pk>/delete/",DeleteArticleView.as_view(), name='delete'),
]