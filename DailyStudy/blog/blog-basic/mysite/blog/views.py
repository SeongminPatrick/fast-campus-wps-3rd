from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import *


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    print('post_detail, pk:%s' % pk )
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


from django.shortcuts import redirect

def post_new(request):
    # uesr = request.user
    # if not user.is_authonticated():
    #     return HttpResponse("로그인하세요")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form 에 아직 author 정보가 없어서 오류가 뜬다
            # 일단 저장을 막아두고 author 을 추가해준 다음에 저장시킨다
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)

    else:
        form = PostForm()
        return render(request, 'post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # instance 로 기존 값을 폼안에 채운다
        # instance 를 넣으면 새로 만드는게 아니라 업데이트한다
        # requeset.Post 앞에 data= 는 생략가능
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        # 이니셜에 저장된 데이터가 폼에 들어가 있다
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
