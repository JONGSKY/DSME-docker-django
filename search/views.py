#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'search/index.html')

@csrf_exempt
def result(request):
    keyword = request.POST.get('keyword')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    name = request.POST.get('name')
    type = request.POST.get('type')
    tags = request.POST.get('tags')

    context = {"data_list" : [name ,type, start_date, end_date, tags]}
    return render(request, 'search/result.html', context)