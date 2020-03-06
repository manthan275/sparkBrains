from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ResumeParser(TemplateView):
	template_name = "resume_parser.html"

class ImageResize(TemplateView):
	template_name = "image_resize.html"

class ImageColoring(TemplateView):
	template_name = "image_coloring.html"

class ImageCropping(TemplateView):
	template_name = "image_cropping.html"

class ImageStiching(TemplateView):
	template_name = "image_stiching.html"
