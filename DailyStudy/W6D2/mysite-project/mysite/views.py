from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
#
# def error(request):
#     error_message = request.Post.get('error_message')
#     context = {
#         'error_message': error_message
#     }
#     return render(request, 'common/error.html', context)