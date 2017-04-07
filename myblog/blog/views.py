# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
# Добавлены render_to_response, Post
from django.shortcuts import render_to_response
from models import Post

def post_list(request):
    """
    Метод строит список Постов (укороченных) сортирует по последней дате записи
    имеет возможность поиска по странице
    """
    listing = Post.objects.all().order_by('-create_date')
    query = request.GET.get('query')
    if query:
        listing = listing.filter(text__icontains=query)
    return render_to_response('post_list.html', {'post_list': listing, 'query': query})

def post_detail(request, pk):
    """
    Метод строит отдельную страницу с расширенной версией Поста
    """
    listing = Post.objects.get(id=pk)
    return render_to_response('post_detail.html', {'post': listing})
