from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class AtricleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'








# def home(request):
#     return render(request,'home.html',{})
