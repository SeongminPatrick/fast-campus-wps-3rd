from django.contrib import messages
from django.shortcuts import render, redirect
from member.forms import SignupForm
from member.models import MyUser
from django.contrib.auth import login as auth_login

def signup2(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            nickname = request.POST['nickname']
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']

            if password != password2:
                messages.error(request, "패스워드가 다릅니다")
                return redirect('member:signup')

            user = MyUser.objects.create_user(
                email=email,
                password=password,
                nickname=nickname,
                last_name=last_name,
                first_name=first_name,
            )

            auth_login(request, user)
            messages.success(request, "회원가입 성공")
            return redirect('blog:post_list')
        else:
            context['form'] = form
    else:
        form = SignupForm()
        context['form'] = form
    return render(request, 'member/signup2.html', context)