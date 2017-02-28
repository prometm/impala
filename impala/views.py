from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'impala/index.html', {})

def specifications(request):
    return render(request, 'impala/specifications.html', {})

def gallery(request):
    return render(request, 'impala/gallery.html', {})

def about(request):
    return render(request, 'impala/about.html', {})

def store(request):
    return render(request, 'impala/store.html', {})