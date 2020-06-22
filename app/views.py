from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from app.models import Grade, Student


def hello(request):
    return HttpResponse("<h1>hello world</h1>")


def grade(request):
    grades = Grade.objects.all()

    return render(request, 'grade_list.html', context=locals())


def students(request, id):
    print(1)
    students = Student.objects.filter(s_grade=id)
    return render(request, 'students.html', locals())


def get_ip(request):

    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
    return HttpResponse('hello %s'% ip)


def login(request):
    return render(request, 'login.html')


def setcookie(request):
    response = HttpResponse()
    response.set_cookie('kk', '11')
    # return HttpResponseRedirect('/app/mine')
    return response


def mine(request):
    uname = request.COOKIES.get('kk')
    return HttpResponse("<h1>Hello %s</h1>" % uname)