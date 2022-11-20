from rest_framework import serializers
from .models import Listen, Sound, Emotion

class ListenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listen
        fields = ('title','body','answer','audio')

class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('title','body','answer','audio')

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('title','body','answer','audio')



