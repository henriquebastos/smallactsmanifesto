import re
from django import template


register = template.Library()
CLASS_PATTERN = re.compile(r'\bclass="[\w\d]*"')

def cssclass(value, arg):
    """
    Replace the attribute css class for Field 'value' with 'arg'.
    """
    attrs = value.field.widget.attrs
    if 'class' in attrs:
        orig = attrs['class']
    else:
        orig = None

    attrs['class'] = arg
    rendered = str(value)

    if orig:
        attrs['class']
    else:
        del attrs['class']

    return rendered
register.filter('cssclass', cssclass)
