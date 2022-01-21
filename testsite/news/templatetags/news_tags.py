from typing import Counter
from django import template
from news.models import Category
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news', distinct=True)).filter(cnt__gt=0, news__is_published=True)
    return {"categories": categories}