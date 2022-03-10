from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('accounts:login'))
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('blog:index'))
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('accounts:login'))
    return render(request, 'accounts/logout.html')


@login_required
def profile_view(request):
    author = request.user
    qs = Post.objects.filter(author__username=author)
    context = {
        'published': qs.filter(published=True),
        'drafts': qs.filter(published=False)
    }
    return render(request, 'accounts/profile.html', context)