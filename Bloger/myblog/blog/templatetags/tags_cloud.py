from django import template
from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tags_cloud.html')
def show_tags(menu_class='content'):
    posts = Tag.objects.all()
    return {"tags": posts, "menu_class": menu_class}

