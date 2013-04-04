# coding: utf-8
from django.utils import six
from django.utils.functional import lazy
from django.utils.safestring import mark_safe


mark_safe_lazy = lazy(mark_safe, six.text_type)

