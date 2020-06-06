from django.shortcuts import render
from article.models import Articles
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.









def index(request):
    templates_name='article/index.html'
    articles= Articles.objects.all()
    content={"articles":articles}
    return render(request,templates_name,content)





class ListArticleView(ListView):
    model = Articles
    context_object_name='articles'
    template_name='article/index.html'


class DetailArticleView(DetailView):
    model=Articles
    template_name='article/detail.html'
    



class CreateArticleView(LoginRequiredMixin,CreateView):
    model=Articles
    fields=('title','content')
    template_name='article/create.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class UpdateArticleView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
        model=Articles
        fields=('title','content')
        template_name='article/update.html'
    
        def form_valid(self,form):
            form.instance.author=self.request.user
            return super().form_valid(form)


        def test_func(self):
            article=self.get_object()
            if self.request.user==article.author:
                return True
            return False



class DeleteArticleView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Articles
    template_name='article/delete.html'
    success_url='/'


    
    def test_func(self):
        article=self.get_object()
        if self.request.user==article.author:
            return True
        return False

        

def about(request):
    templates_name='article/about.html'
    return render(request,templates_name,{'title':'about'})

