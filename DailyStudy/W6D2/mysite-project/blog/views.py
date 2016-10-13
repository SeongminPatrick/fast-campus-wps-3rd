from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects\
        .filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 처음 new에 접근하면 post 방식이 아니라 else로 빠진다 즉 edit.html로 이동
def post_new(request):
    # edit.html에서 돌아오면 post 방식이므로 if true
    if request.method == "POST":
        # PostForm의 인스턴스 생성하여 폼에서 받은 데이터를 PostForm으로 전달
        form = PostForm(request.POST)
        print('1')
        if form.is_valid():
            # PostForm에는 작성자(author) 필드가 없지만, 필드 값이 필요하죠! commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻입니다.
            # - 왜냐하면 작성자를 추가한 다음 저장해야하니까요. 대부분의 경우에는 commit=False를 쓰지 않고 바로 form.save()를 사용해서 저장해요.
            # 다면 여기서는 작성자 정보를 추가하고 저장해야하기 때문에 commit=False를 사용하는 거에요.
            post = form.save(commit=False)
            # 작성자 외 모든 정보는 post가 form에게 받았다.
            # 이번엔 몇 가지 정보 추가
            post.author = request.user
            post.published_date = timezone.now()
            # post에 저장
            post.save()
            print('2')
            # 다시 detail 페이지로 돌아간다
            return redirect('blog:post_detail', pk=post.pk)
    else:
        # PostForm에 requset 정보를 전달하지 않는다.
        form = PostForm()
        print('3')
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # instance 속성으로 덮어씌우기 결정하는듯
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        # instance=post로 PostForm에 원래 있는 데이터를 넣어준다
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})