from django.urls import path
# from . import views
from .views import HomeView,AtricleDetailView


urlpatterns = [
    # path('', views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',AtricleDetailView.as_view(), name="article-detail")
    
]