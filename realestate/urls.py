from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('myproperties',views.myproperties,name='myproperties'),
    path('blog',views.blog,name='blog'),
    path('<int:myproperty_id>', views.myproperty, name='myproperty'),
    path('blog/<slug:slug_id>/',views.blogdetail,name='blogdetail'),
    path('whoweare/<slug:slug_id>/',views.whowearedetail,name='whowearedetail'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('whoweare',views.whoweare,name='whoweare'),
    path('allinone',views.allinone,name='allinone'),
    path('blog',views.blog,name='blog'),
    path('realtors',views.realtors,name='realtors'),
]

