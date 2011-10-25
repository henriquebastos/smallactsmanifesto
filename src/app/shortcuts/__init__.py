# -*- encoding: utf-8 -*-
from django.http import Http404
from django.conf.urls.defaults import url


def route_by_method(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)

    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


def route(regex, GET=None, POST=None, kwargs=None, name=None, prefix=''):
    if not kwargs:
        kwargs = dict()

    if 'GET' in kwargs or 'POST' in kwargs:
        raise RuntimeError("You should not override GET or POST")

    kwargs.update({'GET': GET, 'POST': POST})

    return url(regex, route_by_method, kwargs, name, prefix)
