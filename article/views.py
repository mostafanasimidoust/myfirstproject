from django.shortcuts import render
from . import models


def article(request):
    article=models.Article.objects.all().order_by('date')
    context = {'article' : article}
    return render(request, 'article/maghalat.html',context)
