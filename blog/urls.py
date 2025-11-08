from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    
    # Old url for post:
    # path('<int:id>/', views.post_detail, name='post_detail'),

    # New url for post with SEO-friendly URLs:
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>',
        views.post_detail,
        name='post_detail'
    )
]