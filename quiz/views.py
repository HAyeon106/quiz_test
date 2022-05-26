#from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer

import random

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)

    # serializer에 many=True 옵션을 넣으면 다수의 데이터에 대해서도 직렬화를 한다.
    serializer = QuizSerializer(randomQuiz, many=True)

    return Response(serializer.data)