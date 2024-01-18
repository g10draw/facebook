from django.shortcuts import render

from .forms import PostForm
from .models import Post

# Create your views here.
def home_page(request):
    return render(request, 'blog/home-page.html')

def timeline_page(request):
    form = PostForm()
    posts = Post.objects.all().order_by('-posted_at')
    return render(request, 'blog/timeline.html', 
        {'form': form, 'posts': posts})