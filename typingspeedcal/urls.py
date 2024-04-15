from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('',views.index , name='home'),
    path('home',views.index , name='home'),
    path('home',views.home , name='home'),
    path('login',views.signin , name='login'),
    path('signup',views.signup , name='signup'),
    path('game-letter-crasher',views.game1 , name='game-letter-crasher'),
    path('game-word-scramble',views.game2 , name='game-word-scramble'),
    path('easy-test',views.easy, name='easy-test'),
    path('moderate-test',views.moderate, name='moderate-test'),
    path('hard-test',views.hard, name='hard-test'),

    path('test',views.test,name='test')
    
    
]