from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from datetime import datetime, timedelta

from video.models import Video
from .forms import CategoryForm, VideoForm



def video_list(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'video/video_list.html', {'videos': videos})


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/video_detail.html', {'video': video})

def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('video:video_list')
    else:
        form = CategoryForm()
        return render(request, 'video/category_add.html', {'form': form})


def video_add(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            form.save()
        return redirect('video:video_list')
    else:
        form = VideoForm()
        return render(request, 'video/video_edit.html', {'form': form})


def video_edit(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(data=request.POST, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            form.save()
            return render(request, 'video/video_detail.html', pk=video.pk)
        else:
            pass
    else:
        form = VideoForm(instance=video)

    return render(request, 'video/video_edit.html', {'form': form})
