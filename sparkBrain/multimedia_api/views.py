from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FaceDetection(TemplateView):
	template_name = "face_detection.html"

class ObjectDetection(TemplateView):
	template_name = "object_detection.html"

class ImageClassification(TemplateView):
	template_name = "image_classification.html"

class ImageCaptioning(TemplateView):
	template_name = "image_captioning.html"