from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

from .models import Post
from .forms import PostForm, CommentForm


# def index_view(request):
#     context = {
#         'object_list': Post.objects.exclude(published=False).order_by('-pub_date')
#     }
#     return render(request, 'blog/index.html', context)

class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post

    def get_queryset(self):
        qs = Post.objects.exclude(published=False).order_by('-pub_date')
        return qs


class AboutView(TemplateView):
    template_name = 'blog/about.html'


def post_detail_view(request, slug):
    post_object = get_object_or_404(Post, slug=slug)
    comments = post_object.comments.order_by('-pub_date')
    comment_object = None

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment_object = form.save(commit=False)
            comment_object.post = post_object
            comment_object.save()
            return redirect(post_object)
    else:
        form = CommentForm()

    context = {
        'post': post_object,
        'comments': comments,
        'comment': comment_object,
        'form': form
    }
    return render(request, 'blog/detail.html', context)


@login_required
def post_create_view(request):
    form = PostForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author_id = request.user.pk
        obj.save()
        if obj.published is not True:
            return redirect('accounts:profile')
        return redirect(obj)
    return render(request, 'blog/create-update.html', context)


@login_required
def post_update_view(request, slug):
    post_object = get_object_or_404(Post, slug=slug, author=request.user)
    form = PostForm(request.POST or None, instance=post_object)
    context = {
        'form': form,
        'object': post_object
    }
    if form.is_valid():
        form.save()
        return redirect(post_object)
    return render(request, 'blog/create-update.html', context)


@login_required
def post_delete_view(request, slug):
    post_object = get_object_or_404(Post, slug=slug, author=request.user)
    context = {
        'object': post_object
    }
    if request.method == 'POST':
        post_object.delete()
        return redirect('blog:index')
    return render(request, 'blog/delete.html', context)
