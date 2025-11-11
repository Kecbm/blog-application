from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from .forms import EmailPostForm
from .models import Post

# Old function-based view
def post_list(request):
    posts_list = Post.published.all()

    # Pagination with 3 post per page
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # if page_number is not an integer get the first page
        posts = paginator.page(1)
    
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
        status=Post.Status.PUBLISHED,
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

def post_share(request, post_id):
    # Retrive post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)

        if form.is_valid():
            # Form field passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    
    return render(
        request,
        'blog/post/share.html',
        {'post': post,
        'form': form}
    )

class PostListView(ListView):
    """
    Alternative post list class-based view
    """

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
