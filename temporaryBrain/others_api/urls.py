from django.urls import path,include
from others_api.views import *

urlpatterns = [
	path('resume-parsing', ResumeParser.as_view(), name="resume_parsing"),
	path('image-resize', ImageResize.as_view(), name="image_resize"),
	path('image-coloring', ImageColoring.as_view(), name="image_coloring"),
	path('image-cropping', ImageCropping.as_view(), name="image_cropping"),
	path('image-stiching', ImageStiching.as_view(), name="image_stiching"),
]