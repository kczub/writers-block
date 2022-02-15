from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import PostForm


# function based views
def index_view(request):
    context = {
        'object_list': Post.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'blog/index.html', context)

def post_detail_view(request, pk):
    post_object = get_object_or_404(Post, pk=pk)
    context = {
        'post': post_object
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
        return redirect(obj)
    return render(request, 'blog/create-update.html', context)


@login_required
def post_update_view(request, pk):
    post_object = get_object_or_404(Post, pk=pk, author=request.user)
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
def post_delete_view(request, pk):
    post_object = get_object_or_404(Post, pk=pk, author=request.user)
    context = {
        'object': post_object
    }
    if request.method == 'POST':
        post_object.delete()
        return redirect('blog:index')
    return render(request, 'blog/delete.html', context)