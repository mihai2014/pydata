
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('posts', views.home, name = 'about'),  #redirect...
    path('posts/', views.home, name = 'about'), #redirect...
    path('about', views.about, name = 'about'),
    path('about/', views.about, name = 'about'),
    path('book/<path:file_path>', views.book, name="book"), 
    #path('html/<path:file_path>', views.html, name="html"),
]

#handler404 = 'notebooks.views.error404'
#handler404 = views.error404
