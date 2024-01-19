from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer

# Create your views here.
def home_page(request):
    return render(request, 'blog/home-page.html')

def timeline_page(request):
    form = PostForm()
    posts = Post.objects.all().order_by('-posted_at')
    return render(request, 'blog/timeline.html', 
        {'form': form, 'posts': posts})

@api_view(['POST'])
@login_required
def create_post(request):
    title = request.POST.get('title')
    image = request.FILES.get('image')

    new_post = Post(title=title, author=request.user)

    if image:
        new_post.image = image
    
    new_post.save()

    serializer = PostSerializer(new_post)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
