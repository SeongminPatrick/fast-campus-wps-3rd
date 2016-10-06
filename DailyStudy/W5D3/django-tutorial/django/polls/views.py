from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Choice, Question
from django.http import Http404
from django.urls import reverse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     # pu_date 역순으로 정렬하고 5개 추출
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # 장고 템플릿 폴더에서 index.html 파일을 가져온다
#     template = loader.get_template('index.html')
#     # 템플릿을 렌더릴 할 때 사용할 변수 dictionary
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # Http형식으로 응답을 돌려준다. 내용은 template을 context와 request를 사용해서 렌더링한 결과
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'index.html', context)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'detail.html', {'question': question})

def detail(request, question_id):
    # 404 에러가 아니면 question = Question.objects.get(pk=question_id)를 출력한다
    question = get_object_or_404(Question, pk=question_id)
    # detail.html에 request와 question 키를 가진 dictionary를 렌더링해서 전달한다
    return render(request, 'detail.html', {'question': question})



# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def vote(request, question_id):
    # 404 오류가 없으면 Question.objects.get(pk=question) 을 question 에 대입한다
    question = get_object_or_404(Question, pk=question_id)
    from IPython import embed;embed()
    try:
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)

    # KeyError가 나면 detail.html 에 question 과 error 메시지와 request를 렌더링해서 전달한다
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice',
        })
    # KeyError 가 없으면 실행..
    else:
        # selected_choice 의 votes 변수를 1 증가시킨다
        selected_choice.votes += 1
        selected_choice.save()
        # polls 의 results name의 url로 qusstion.id와 보낸다
        redirect_url = reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(redirect_url)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})