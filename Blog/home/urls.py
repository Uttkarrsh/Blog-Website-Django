from django.urls import path
from .views import *
urlpatterns = [
   path('', home, name="home"),
   path('login/',login_view, name="login_view"),
   path('register/',register_view, name="register_view"),
   path('addblog/',add_blog, name="add_blog"),
   path('blogdetail/<slug>',blog_detail, name="blog_detail"),
   path('seeblog/', see_blog, name="see_blog"),
   path('delete/<id>', delete, name="blog_delete"),
   path('update/<slug>', update, name="blog_update"),
   path('logout', logout_view, name="logout_view"),
]