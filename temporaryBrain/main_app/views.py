from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Homepage(TemplateView):
	template_name = "index.html"
	def get_context_data(self,*args,**kwargs):
		print("In")
		return {}

class AboutUs(TemplateView):
	template_name = "about_us.html"


class Blog(TemplateView):
	template_name = "blog.html"

class Contact(TemplateView):
	template_name = "contact.html"