from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import PostForm
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
def home_page(request):
    return render(request, 'blog/home-page.html')

def timeline_page(request):
    form = PostForm()
    posts = Post.objects.prefetch_related('comments__user').order_by('-posted_at')
    return render(request, 'blog/timeline.html', 
        {'form': form, 'posts': posts})

def profile_page(request):
    return render(request, 'blog/profile-page.html')

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


@api_view(['PUT'])
@login_required
def update_like(request):
    post_id = request.data.get('post_id')
    user = request.user

    post = Post.objects.get(pk=post_id)

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    
    post.save()

    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@login_required
def add_comment(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    data = request.data
    new_comment = Comment(user=user, post=post, text=data.get('comment'))
    new_comment.save()

    serializer = CommentSerializer(new_comment)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    