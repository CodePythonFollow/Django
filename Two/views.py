from time import sleep

# from django.core.cache import cache
from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.cache import cache_page


def hello(request):
    result = caches['redis_cache'].get('hello')
    if result:
        print(1)
        return HttpResponse(result)


    data = {
        'arr': ['1', '2', '3', '4']
    }
    sleep(1)
    response = render(request, 'text_cache.html', context=data)
    caches['redis_cache'].set('hello', response.content, timeout=60)

    return response


@cache_page(timeout=60, cache='redis_cache', key_prefix='abcd')
def get_redis(request):
    data = {
        'arr': ['1', '2', '3', '4']
    }
    sleep(1)
    response = render(request, 'text_cache.html', context=data)
    return response
