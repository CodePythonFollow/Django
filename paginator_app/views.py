from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from app.models import Student


def hello(request):
    return HttpResponse("Hello paginator")


# 分页器
def getdata(request):
    students = Student.objects.all()
    page = request.GET.get("num", 1)
    per_page = request.GET.get("per_page", 10)
    paginator = Paginator(students, per_page=per_page)
    # print(paginator.object_list)
    data = {
        "data": paginator.page(page)
    }
    return render(request, 'get_data.html', context=data)