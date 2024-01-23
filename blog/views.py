from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import PostForm
from .models import Post, Comment, Follow
from auth_manager.models import CustomUser
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
def home_page(request):
    return render(request, 'blog/home-page.html')

@login_required
def timeline_page(request):
    form = PostForm()
    following = request.user.following.all()
    followers = request.user.followers.all()

    following_ids = [follow_obj.following.id for follow_obj in following] + [request.user.id]
    posts = Post.objects.filter(
        author__id__in=following_ids).prefetch_related(
        'comments__user').order_by('-posted_at')
    
    # People To Follow
    to_follow = CustomUser.objects.filter(
        is_superuser=False).exclude(pk__in=following_ids)
    return render(request, 'blog/timeline.html', 
        {
            'form': form, 
            'posts': posts,
            'followers': followers,
            'following': following,
            'to_follow': to_follow,
        }
    )

@login_required
def profile_page(request, user_id):
    profile_user = CustomUser.objects.get(pk=user_id)
    posts = Post.objects.filter(author=profile_user).order_by('-posted_at')
    am_i_following = Follow.objects.filter(
        follower=request.user, following=profile_user).exists()
    following = profile_user.following.all()
    followers = profile_user.followers.all()
    return render(
        request, 
        'blog/profile-page.html', 
        {
            'profile': profile_user, 
            'posts': posts,
            'am_i_following': am_i_following,
            'followers': followers,
            'following': following,
        }
    )

@login_required
def handle_follow(request, user_id):
    profile_user = CustomUser.objects.get(pk=user_id)
    following = Follow.objects.filter(
        follower=request.user, following=profile_user)
    if following:
        following.delete()
        messages.error(request, f'Unfollowed {profile_user.username}')
    else:
        new_record = Follow.objects.create(
            follower=request.user, following=profile_user
        )
        messages.success(request, f'Following {profile_user.username}')
    return redirect('profile-page', user_id=user_id)

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
    