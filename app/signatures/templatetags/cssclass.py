import re
from django import template


register = template.Library()
CLASS_PATTERN = re.compile(r'\bclass="[\w\d]*"')

def cssclass(value, arg):
    """
    Replace the attribute css class for Field 'value' with 'arg'.
    """
    attrs = value.field.widget.attrs
    orig = attrs['class'] if 'class' in attrs else None

    attrs['class'] = arg
    rendered = str(value)

    if orig:
        attrs['class']
    else:
        del attrs['class']

    return rendered
register.filter('cssclass', cssclass)
