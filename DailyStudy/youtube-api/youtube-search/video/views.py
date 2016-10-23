import json
from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

# youtube 예시문 상당 참조해서 커스텀화
DEVELOPER_KEY = "AIzaSyDeFsX6-gtB-iA_xslFF0OVDJfEqWk-Wb0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(keyword, page_token, max_results=10):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=max_results,
    pageToken=page_token,
  ).execute()

  return search_response



def search(request):
    # keyword = request.GET.get('keyword')
    # response = youtube_search(keyword)
    # Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는
    # JSON Encoding 이라 부른다. JSON 인코딩을 위해서는 우선 json 라이브러리를
    # import 한 후, json.dumps() 메서드를 써서 Python Object를 문자열로 변환하면 된다.
    # print(json.dumps(response, indent=2, sort_keys=True))
    #
    # context = {
    #     'keyword': keyword,
    #     'response': response,
    # }
    context = {}
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:
        response = youtube_search(keyword, page_token)
        context['keyword'] = keyword
        context['response'] = response
    return render(request, 'video/search.html', context)