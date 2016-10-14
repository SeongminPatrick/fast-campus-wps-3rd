from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login, logout as auth_logout
from member.models import MyUser


def signup(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            nickname = request.POST['nickname']
            lastname = request.POST['lastname']
            firstname = request.POST['firstname']
        except KeyError:
            return HttpResponse('필드에 없는 값이 있습니다')

        if password != password2:
            messages.error(request, "패스워드가 다릅니다")
            return redirect('member:signup')

        user = MyUser.objects.create_user(
            email=email,
            password=password,
            nickname=nickname,
            last_name=lastname,
            first_name=firstname,
        )
        # 생성한 user로 로그인
        auth_login(request, user)
        messages.success(request, "로그인 성공")
        redirect('blog:post_list')
    else:
        return render(request, 'member/signup.html', {})

    return redirect('blog:post_list')


