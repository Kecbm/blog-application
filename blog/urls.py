from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    
    # Old url for post:
    # path('<int:id>/', views.post_detail, name='post_detail'),

    # New url for post with class-based views:
    # path('', views.PostListView.as_view(), name='post_list'),

    # New url for post with SEO-friendly URLs:
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>',
        views.post_detail,
        name='post_detail'
    ),
    # Url for share post
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path(
        '<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
    path(
        'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
    )
]