from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request, 'viewcrud/funccrud.html', {'blogs': blogs, 'posts':posts})

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})
    return

def update(request, pk):
    blog = get_object_or_404 (Blog, pk = pk)
    form = NewBlog (request.POST, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'viewcrud/new.html', {'form':form})

def delete (request, pk):
    blog = get_object_or_404 (Blog, pk = pk)
    blog.delete()
    return redirect('home')


