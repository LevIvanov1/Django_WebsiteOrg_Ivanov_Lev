from django.shortcuts import render
from .models import News

def index(request):
        news = News.objects.order_by('-pub_date')[:3] 
        return render(request, 'news_site_company/index.html', {'news': news})