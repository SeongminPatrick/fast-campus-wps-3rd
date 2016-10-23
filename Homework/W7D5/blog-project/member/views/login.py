from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def login(request):
    # get으로받은 이전경로 next에 저장
    next = request.GET.get('next')
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            # 데이터베이스와 계정일치여부 확인
            # print(1)
            user = auth_authenticate(username=username, password=password)
            # print (user)
        except KeyError:
            return HttpResponse('username과 password는 필수입니다')

        if user is not None:
            # print(2)
            # user 정보로 로그인처리
            auth_login(request, user)
            # message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS
            messages.success(request, "로그인 성공")
            # 로그인 이전 화면으로 리다이렉트
            return redirect(next)
        else:
            # message.level == DEFAULT_MESSAGE_LEVELS.ERROR
            messages.error(request, "로그인 실패")
            return render(request, 'member/login.html', {})
    else:
        # print(3)
        return render(request, 'member/login.html')

def login_facebook(request):

    if request.GET.get('error'):
        messages.error(request, '페이스북 로그인을 취소했습니다')
        return redirect('member:login')

    if request.GET.get('code'):


        from django.conf import settings
        import requests
        import json
        APP_ID = settings.FACEBOOK_APP_ID
        SECRET_CODE = settings.FACEBOOK_SECRET_CODE
        REDIRECT_URL = 'http://127.0.0.1:8000/member/login/facebook/'
        code = request.GET.get('code')

        # access token을 받아내자
        url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token?' \
                                   'client_id={client_id}&' \
                                   'redirect_uri={redirect_uri}&' \
                                   'client_secret={client_secret}&' \
                                   'code={code}'.format(
                                        client_id=APP_ID,
                                        redirect_uri=REDIRECT_URL,
                                        client_secret=SECRET_CODE,
                                        code=code,
                                    )
        # 해당 url로 get 요청을 보냄
        r = requests.get(url_request_access_token)
        dict_access_token = r.json()
        print(json.dumps(dict_access_token, indent=2))
        ACCESS_TOKEN = dict_access_token['access_token']

        # debug token을 받아내자
        APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
            app_id=APP_ID,
            secret_code=SECRET_CODE,
        )

        url_debug_token = 'https://graph.facebook.com/debug_token?' \
                          'input_token={it}&' \
                          'access_token={at}'.format(
            it=ACCESS_TOKEN,
            at=APP_ACCESS_TOKEN
        )
        r = requests.get(url_debug_token)
        dict_debug = r.json()
        print(json.dumps(dict_debug, indent=2))
        USER_ID = dict_debug['data']['user_id']
        print('USER_ID : %s' % USER_ID)

        # 페이북에서 데이터 요청시 그래프 api 를 활용한다

        url_request_user_info = 'https://graph.facebook.com/' \
                                '{user_id}?' \
                                'fields=id,picture,name,first_name,last_name,timezone,email,birthday&' \
                                'access_token={access_token}'.format(
                                    user_id=USER_ID,
                                    access_token=ACCESS_TOKEN,
                                )
        r = requests.get(url_request_user_info)
        dict_user_info = r.json()
        print(json.dumps(dict_user_info, indent=2))

        user = auth_authenticate(user_info=dict_user_info)
        if user is not None:
            auth_login(request, user)
            messages.success(request, '페이스북 로그인 성공')
            return redirect('blog:post_list')
        else:
            messages.error(request, '페이스북 로그인 실패')
            return redirect('member:login')