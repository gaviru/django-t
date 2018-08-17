from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Post

#from django.shortcuts import get_object_or_404, redirect, render
#from utils.str_util import StrUtil
#from .forms import PostForm    # CBV 방식을 사용하면 form 크래스는 필요없음
#import logging

# Create your views here.

# CBV 방식 ListView
class PostListView(ListView):
    #model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'postL'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()
                            ).order_by('-published_date')


# CBV 방식 DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# CBV 방식 CreateView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']
    #initial = {'slug': 'auto-filling-do-not-input'}
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        return super(PostCreateView, self).form_valid(post)

    def get_success_url(self):
        post_row = Post.objects.order_by('-id').first()
        return reverse_lazy('post_detail', args = (post_row.id,))


# CBV 방식 UpdateView
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'blog/post_edit.html'
    #success_url = reverse_lazy('post_list') #전달인자가 없을땐 여기를 사용. 함수는 제거
    
    def get_success_url(self):
        return reverse_lazy('post_detail', args = (self.object.id,))



#######################################################################
## FBV 방식 구현
#######################################################################

# FBV 방식 ListView
# def post_list(request):
#     qs = Post.objects.filter(published_date__lte=timezone.now()
#                     ).order_by('-published_date')

#     PostL = get_context_data(qs)

#     # paginator = Paginator(qs, 5) # Show 5 PostL per page
#     # page = request.GET.get('page')
#     # try:
#     #     PostL = paginator.page(page)
#     # except PageNotAnInteger:
#     #     # If page is not an integer, deliver first page.
#     #     PostL = paginator.page(1)
#     # except EmptyPage:
#     #     # If page is out of range (e.g. 9999), deliver last page of results.
#     #     PostL = paginator.page(paginator.num_pages)

#     return render(request, 'blog/post_list.html',{
#         'postL': qs,
#     })


# # FBV 방식 DetailView
# def post_detail(request, pk):
#     postObj = get_object_or_404(Post, pk=pk)
#     postObj.text = StrUtil.strTohtml(postObj.text)
#     #tt = StrUtil.strTohtml("22")
#     #try:
#     #    qs = Post.objects.get(pk=pk)
#     #except Post.DoesNotExist:
#     #    raise Http404   #Page Not Found : from django.http import Http404
#     return render(request, 'blog/post_detail.html', {
#         'post': postObj,
#     })


# FBV 방식 CreateView
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {
#         'form': form,
#     })


# FBV 방식 UpdateView
# def post_edit(request, pk):
#     qs = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=qs)
#         if form.is_valid():
#             qs = form.save(commit=False)
#             qs.author = request.user
#             qs.published_date = timezone.now()
#             qs.save()
#             return redirect('post_detail', qs.pk)
#     else:
#         form = PostForm(instance=qs)

#     return render(request, 'blog/post_edit.html', {
#         'form': form,
#     })