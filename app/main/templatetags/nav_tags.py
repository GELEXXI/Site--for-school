from django import template

from main.models import Post


register = template.Library()


@register.simple_tag()
def tag_navs():
    return Post.objects.all()
