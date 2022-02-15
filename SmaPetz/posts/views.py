from multiprocessing import context
from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def home_view(request):
    #a query set to get all the posts
    qs = Post.objects.all()
    #pass the query set to the template
    context = {
        'hello':'hello world',
        'qs':qs,
    }
    return render(request, 'posts/main.html', context)

def post_view(request):
    qs = Post.objects.all()
    data = serializers.serialize('json', qs)
    return JsonResponse({'data':data})