from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'search/index.html')

def result(request):
    search_keyword = request.GET['keyword']
    example_data = search_keyword+"에 대한 결과물이 나올 예정입니다."
    context = {"data_list": example_data}
    return render(request, "search/result.html", context)
