from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.views.generic import ListView
# Create your views here.

def postIndex(request):
	post = Post.objects.all()
	return render(request, 'index.html', {'post':post})
def postID(request, slug):
	posted = get_object_or_404(Post, slug = "top-laptops-2022")
	posts = Post.objects.filter(slug = slug)
	if posts.exists():
		posts = posts.first()
	else:
		return HttpResponse("<h1>page not found</h1>")
	return render(request, 'posts/post.html', {'posted':posted, 'postid':posts})
def indexec(request):
	posts = get_object_or_404(Post, id = 7)
	one = Post.objects.latest('id') 
	two = get_object_or_404(Post, id = 10)
	three = get_object_or_404(Post, id = 8)
	mostone = get_object_or_404(Post, id = 11)
	mosttwo = get_object_or_404(Post, id = 7)
	mostthree = get_object_or_404(Post, id = 31)
	return render(request, 'index.html',  {'posted':posts, 'one':one, 'two':two, 'three':three, 'mostone':mostone, 'mosttwo':mosttwo, 'mostthree':mostthree})
def category(request):
		post = Post.objects.all()
		return render(request, 'Category.html', {'posts':post})
def technology(request):
	post = Post.objects.all()
	return render(request, 'technology.html', {'posts':post})

def general(request):
	post = Post.objects.all()
	return render(request, 'general.html', {'posts':post})
	
def health_fitness(request):
	post = Post.objects.all()
	return render(request, 'health_fitness.html', {'posts':post})
	
def unsolved(request):
	post = Post.objects.all()
	return render(request, 'unsolved.html', {'posts':post})
	
def self_improvement(request):
	post = Post.objects.all()
	return render(request, 'self_improvement.html', {'posts':post})
def contact(request):
		return render(request, 'Contact.html')
def PrivacyPolicy(request):
		return render(request, 'PrivacyPolicy.html')