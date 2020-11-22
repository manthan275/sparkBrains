from django.urls import path,include
from main_app.views import *

urlpatterns = [
	path('',Homepage.as_view(),name="homepage"),
	path('about-us', AboutUs.as_view(), name="about_us"),
	path('blog', Blog.as_view(), name="blog"),
	path('contact-us', Contact.as_view(), name="contact_us"),
]