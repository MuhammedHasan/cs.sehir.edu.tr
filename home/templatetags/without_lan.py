from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name="withoutLan")
def without_lan(value):
    return value[3:]
