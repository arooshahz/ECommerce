from django import template

register = template.Library()


@register.simple_tag
def get_url(category, page_number):
    return category.get_absolute_url(page_number)
