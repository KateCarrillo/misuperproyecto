from django.shortcuts import render
from .models import Post
# Create your views here.

def bloglista(request):
	milista = Post.objects.all()
	return render(request, 'blog/plantillablog.html', {"milista": milista})
