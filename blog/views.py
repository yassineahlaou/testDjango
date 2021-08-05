from django.shortcuts import  render
from django.http import HttpResponse
from .models import Accueil
from django.views.generic import DetailView
from .models import Categorie
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    articles = Accueil.objects.all()
    category_list = Categorie.objects.all()
    #Pagination
    p=Paginator(articles,4)
    page=request.GET.get('page')
    list_articles=p.get_page(page)

    context = {'articles': articles , 'category_list':category_list, 'list_articles':list_articles}

    return render (request , 'blog/blog.html', context)



def CategoryDetailView(request,you):
    category_articles = Accueil.objects.filter(categorie__name=you)
    category_list = Categorie.objects.all()
    l = Paginator(category_articles, 3)
    page= request.GET.get('page')
    list_category = l.get_page(page)

    context = {'category_articles': category_articles , 'you':you.title(),'category_list':category_list,'list_category':list_category}
    return render(request, 'categorie/categorie.html', context)



class Articledetail(DetailView):
    model = Accueil
    context_object_name = 'art'

    template_name = 'article/article.html'
    def get_context_data(self, *args, **kwargs):
        category_list=Categorie.objects.all()
        context=super(Articledetail,self).get_context_data(*args,**kwargs)
        context["category_list"]=category_list
        return context







