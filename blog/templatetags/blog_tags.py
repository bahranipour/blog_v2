from django import template
from ..models import Post,Category

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/post_latest.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-created_at')[:count]
    return {'latest_posts':latest_posts}

@register.inclusion_tag('blog/post_category.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories':categories}