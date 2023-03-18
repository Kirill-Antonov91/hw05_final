from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import CommentForm, PostForm
from .models import Follow, Group, Post, User

POSTS_PER_PAGE = 10


def get_page(page_number, posts):
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    return page_obj


@cache_page(20, key_prefix="index_page")
def index(request):
    posts = Post.objects.select_related("group", "author")
    return render(
        request,
        "posts/index.html",
        {"page_obj": get_page(request.GET.get("page"), posts)},
    )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related("author")
    return render(
        request,
        "posts/group_list.html",
        {"group": group, "page_obj": get_page(request.GET.get("page"), posts)},
    )


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.select_related("group")
    post_count = author.posts.count
    following = (
        request.user.is_authenticated
        and Follow.objects.filter(user=request.user, author=author).exists()
    )
    return render(
        request,
        "posts/profile.html",
        {
            "author": author,
            "page_obj": get_page(request.GET.get("page"), posts),
            "following": following,
            "post_count": post_count
        },
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related("author", "group"), id=post_id
    )
    comments = post.comments.select_related("author")
    form = CommentForm()
    author = request.user.id
    return render(
        request,
        "posts/post_detail.html",
        {
            "post": post,
            "author": author,
            "form": form,
            "comments": comments,
        },
    )


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("posts:profile", post.author.username)
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(
        request.POST or None, files=request.FILES or None, instance=post
    )
    context = {
        "form": form,
        "is_edit": True,
    }
    if request.user != post.author:
        return redirect("posts:post_detail", post_id=post.id)
    if not form.is_valid():
        return render(request, "posts/create_post.html", context)
    form.save()
    return redirect("posts:post_detail", post_id=post.id)


@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = get_object_or_404(Post, id=post_id)
        comment.save()
    return redirect("posts:post_detail", post_id=post_id)


@login_required
def follow_index(request):
    posts = Post.objects.filter(
        author__following__user=request.user
    ).select_related("author", "group")
    return render(
        request,
        "posts/follow.html",
        {
            "page_obj": get_page(request.GET.get("page"), posts),
        },
    )


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if request.user != author:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect("posts:profile", username=username)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    Follow.objects.filter(user=request.user, author=author).delete()
    return redirect("posts:profile", username=username)
