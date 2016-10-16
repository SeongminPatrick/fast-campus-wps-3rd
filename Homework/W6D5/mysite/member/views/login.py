from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login


def login(request):
    next = request.GET.get('next')
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = auth_authenticate(username=username, password=password)
        except KeyError:
            return HttpRequest("unername과 password를 입력하세요")

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인성공')
            return redirect(next)
        else:
            messages.error(request, '로그인실패')
            return render(request, 'member/login.html')
    else:
        return render(request, 'member/login.html')
