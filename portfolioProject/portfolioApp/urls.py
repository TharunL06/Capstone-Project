from django.urls import path
from portfolioApp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('login',views.handlelogin,name='login'),
    path('signup',views.signup,name='signup')
]
