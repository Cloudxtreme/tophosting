from django import template
from django.conf import settings

register = template.Library()

@register.filter
def format_features(value):
    lines = value.splitlines()
    output_html = ''
    for line in lines:
        output_html += '<span class="check">&#10003;</span> ' + line + '<br />'
    return output_html
