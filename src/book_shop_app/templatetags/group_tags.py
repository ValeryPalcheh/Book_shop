from django import template
from book_shop_app import models as book_models


register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()



@register.inclusion_tag('book_shop_app/sale_list.html')
def newest_items():
    newest_books = book_models.Book.objects.order_by('-pk')
    return {"items": newest_books[0:5]}

@register.inclusion_tag('book_shop_app/sale_list.html')
def oldest_items():
    oldest_books = book_models.Book.objects.order_by('pk')
    return {"items": oldest_books[0:5]}