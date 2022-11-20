from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Listen, Sound, Emotion
from .serializers import ListenSerializer, SoundSerializer, EmotionSerializer
import random

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

@api_view(['GET'])
def ListenQuiz(request, id):
    totalQuizs = Listen.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = ListenSerializer(randomQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def EmotionQuiz(request, id):
    totalQuizs = Emotion.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = EmotionSerializer(randomQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SoundQuiz(request, id):
    totalQuizs = Sound.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = SoundSerializer(randomQuizs, many=True)
    return Response(serializer.data)

