from django.contrib import messages
import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from member.apis import facebook
from django.urls import reverse
import json

__all__ = [
    'friends_ranking',
]

def friends_ranking(request):

    if request.GET.get('error'):
        return HttpResponse('사용자 로그인 거부')

    if request.GET.get('code'):
        code = request.GET.get('code')
        REDIRECT_URL = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:friends_ranking'),
        )

        access_token = facebook.get_access_token(code, REDIRECT_URL)
        # return HttpResponse('%s<br>%s' % (REDIRECT_URL, access_token))
        user_id = facebook.get_user_id_from_token(access_token)
        # facebook에서 comment 하위 속성은 { } 형식으로 불러온다
        # {{}} 형식을 사용해야 format() 형식에서 사용 가능하다
        url_request_feed = 'https://graph.facebook.com/v2.8/{user_id}/feed?' \
                           'fields=picture,link,comments{{from{{picture,name}},message,comments}}&limit=1000&since=2014-01-01&' \
                           'access_token={access_token}'.format(
            user_id=user_id,
            access_token=access_token,

        )
        r = requests.get(url_request_feed)
        dic_feed_info = r.json()
        json_data = json.dumps(dic_feed_info, indent=2)
        print(json_data)
        return HttpResponse(json_data)