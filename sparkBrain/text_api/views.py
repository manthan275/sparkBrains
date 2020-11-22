from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class SentimentAnalysis(TemplateView):
	template_name = "sentiment_analysis.html"

class EmotionAnalysis(TemplateView):
	template_name = "emotion_analysis.html"

class HateSpeechAnalysis(TemplateView):
	template_name = "hate_speech.html"

class SarcasmDetection(TemplateView):
	template_name = "sarcasm_detection.html"
