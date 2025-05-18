from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import RegisterForm, NewsForm,  CommentForm  
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .forms import CommentForm


def index(request):
        news = News.objects.order_by('-pub_date')[:3]
        return render(request, 'news_site_company/index.html', {'news': news})

@login_required
def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(news=news_item, user=request.user, text=comment_form.cleaned_data['text'])
            comment.save()
            return redirect('news_detail', news_id=news_id)
    else:
        comment_form = CommentForm()
    return render(request, 'news_site_company/news_detail.html', {'news_item': news_item, 'comment_form': comment_form})

def news_list(request):
    sort_by = request.GET.get('sort', '-pub_date')
    query = request.GET.get('q')

    if query:
        news = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by(sort_by)
    else:
        news = News.objects.order_by(sort_by)

    return render(request, 'news_site_company/news_list.html', {'news': news, 'query': query})

def contact(request):
        return render(request, 'news_site_company/contact.html')

def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
        return render(request, 'news_site_company/register.html', {'form': form})

@login_required
def profile(request):
    comments = Comment.objects.filter(user=request.user).order_by('-created_date')
    return render(request, 'news_site_company/profile.html', {'comments': comments})

def news_search(request):
        query = request.GET.get('q')

        if query:
            news = News.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-pub_date')
        else:
            news = News.objects.order_by('-pub_date')

        return render(request, 'news_site_company/news_list.html', {'news': news, 'query': query})

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user.username
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_site_company/news_create.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def news_edit(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news_id=news_id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_site_company/news_edit.html', {'form': form, 'news': news})

@login_required
@user_passes_test(is_staff)
def news_delete(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    return redirect('news_list')