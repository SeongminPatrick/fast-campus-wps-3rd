from django.contrib import messages
from django.shortcuts import render, redirect

from video.models import Video
__all__ = [
    'add_bookmark',
    'bookmark_list',
    'bookmark_detail',
    'bookmark_delete',
]

def add_bookmark(request):
    path = request.POST.get('path')
    try:
        kind = request.POST['kind']
        youtube_id = request.POST['youtube_id']
        title= request.POST['title']
        description = request.POST['description']
        published_date = request.POST['published_date']
        thumbnail_url = request.POST['thumbnail_url']

        Video.objects.create(
            kind=kind,
            youtube_id=youtube_id,
            title=title,
            description=description,
            published_date=published_date,
            thumbnail_url=thumbnail_url,
        )
        msg = '%s 영상을 북마크에 저장했습니다' % Video.title
    except Exception as e:
        msg = 'Exception! %s (%s)' % (e, e.args)

    messages.success(request, msg)

    if path:
        return redirect(path)
    else:
        return redirect('video:bookmark_list')


def bookmark_list(request):
    videos = Video.objects.all().order_by('-add_date')
    return render(request, 'video/bookmark_list.html', {'videos': videos})


def bookmark_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'video/bookmark_detail.html', {'video': video})

def bookmark_delete(request, pk):
    video = Video.objects.get(pk=pk)
    msg = '%s 영상을 북마크에서 삭제했습니다' % video.title
    video.delete()
    messages.success(request, msg)
    return redirect('video:bookmark_list')