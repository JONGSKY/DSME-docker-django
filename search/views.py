from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'search/index.html')

def result(request):
    search_keyword = request.GET['keyword']
    start_date = request.GET['start-date']
    end_date = request.GET['end-date']
    name = request.GET['name']
    type = request.GET['type']
    tags = request.GET['tags']

    context = {"data_list": search_keyword+"에 대한 결과물이 나올 예정입니다."}
    return render(request, "search/result.html", context)
