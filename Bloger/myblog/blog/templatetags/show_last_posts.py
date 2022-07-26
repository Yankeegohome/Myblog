from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/show_last_posts.html')
def show_posts(menu_class='content'):
    posts = Post.objects.all().order_by("-created_at")[0:5]
    return {"posts": posts, "menu_class": menu_class}


@register.inclusion_tag('blog/banner.html')
def show_banner(menu_class='owl-banner owl-carousel'):
    posts = Post.objects.all().order_by("-created_at")[0:5]
    return {"posts": posts, "menu_class": menu_class}