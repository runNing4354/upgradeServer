from django.urls import path, include
from .views import helloAPI, ListenQuiz, SoundQuiz, EmotionQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("listen/<int:id>/", ListenQuiz),
    path("sound/<int:id>/", SoundQuiz),
    path("emotion/<int:id>/", EmotionQuiz),

]