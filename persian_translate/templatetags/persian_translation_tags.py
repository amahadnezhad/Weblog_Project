from django import template

register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    value.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
