from django.contrib import admin
from .models import Listen, Sound, Emotion
# Register your models here.

admin.site.register(Listen)
admin.site.register(Sound)
admin.site.register(Emotion)