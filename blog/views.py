from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from utils.str_util import StrUtil

# Create your views here.

def post_list(request):
    qs = Post.objects.filter(published_date__lte=timezone.now()
                    ).order_by('published_date')

    return render(request, 'blog/post_list.html',{
        'postL': qs,
    })

def post_detail(request, pk):
    postObj = get_object_or_404(Post, pk=pk)
    postObj.text = StrUtil.strTohtml(postObj.text)
    #tt = StrUtil.strTohtml("22")
    #try:
    #    qs = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #    raise Http404   #Page Not Found : from django.http import Http404
    return render(request, 'blog/post_detail.html', {
        'post': postObj,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form': form,
    })

def post_edit(request, pk):    
    qs = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.author = request.user
            qs.published_date = timezone.now()
            qs.save()
            return redirect('post_detail', qs.pk)
    else:
        form = PostForm(instance=qs)

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })