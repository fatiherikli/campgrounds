from django.template import Library

register = Library()

@register.filter()
def replace_comma(value, new="."):
    return str(value).replace(",", new)
