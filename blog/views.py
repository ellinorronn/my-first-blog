from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
	return render(request, 'blog/index.html')

def blog(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = PostForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)		
		else:
			form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
#	user = get_object_or_404(User, user=user)
	return render(request, 'blog/about.html')

