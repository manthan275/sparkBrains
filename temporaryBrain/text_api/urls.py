from django.urls import path,include
from text_api.views import *


urlpatterns = [
	path('sentiment-analysis',SentimentAnalysis.as_view(),name="sentiment_analysis"),
	path('emotion-analysis',EmotionAnalysis.as_view(),name="emotion_analysis"),
	path('hate-speech-analysis',HateSpeechAnalysis.as_view(),name="hate_speech_analysis"),
	path('sarcasm-detection', SarcasmDetection.as_view(), name="sarcasm_detection"),
]