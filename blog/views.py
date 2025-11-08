from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    """
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No post found.')
    """
    
    # Old structure
    """
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )   
    """
    
    # New structure with canonical urls
    post = get_object_or_404(
        Post,
        slug=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
