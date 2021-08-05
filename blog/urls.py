from django.urls import path
from . import views
from blog.views import CategoryDetailView,Articledetail

urlpatterns = [

    path('',views.home,name='home'),
path('categorie/<str:you>/',CategoryDetailView,name='categorie'),
    path('article/<int:pk>/',Articledetail.as_view(),name='article')
]