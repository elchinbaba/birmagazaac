from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from . import forms
from . import models

# Create your views here.

def magaza(request):
    magazas = models.Magaza.objects.all()
    context = {
        'magazas': magazas
    }
    return render(request, 'magaza/magaza.html', context)
def create(request):
    if request.method == "POST":
        form = forms.MagazaForm(request.POST)
        if form.is_valid:
            try:
                magaza = form.save()
                return HttpResponseRedirect(magaza.get_absolute_url())
            except:
                messages.error
    else:
        form = forms.MagazaForm()

    context = {
        'form': form
    }
    return render(request, 'magaza/create.html', context)
def detail(request, slug):
    magaza = get_object_or_404(models.Magaza, slug=slug)
    posts = models.Post.objects.filter(magaza=magaza)

    context = {
        'posts': posts,
        'magaza': magaza,
    }
    return render(request, 'magaza/detail.html', context)

def post_create(request, slug):
    magaza = models.Magaza.objects.get(slug=slug)

    if request.method == "POST":
        form = forms.PostForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            post = form.save(commit=False)
            post.magaza = magaza
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = forms.PostForm()
        form.magaza = magaza
    
    context = {
        'magaza': magaza,
        'form': form,
    }
    return render(request, 'magaza/post/create.html', context)

def post_detail(request, slug, pk):
    post = get_object_or_404(models.Post, id=pk)

    magaza = models.Magaza.objects.get(slug=slug)
    post.magaza = magaza
    context = {
        'magaza': magaza,
        'post': post,
    }
    return render(request, 'magaza/post/detail.html', context)