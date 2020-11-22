from django.urls import path,include
from multimedia_api.views import *

urlpatterns = [
	path('face-detection', FaceDetection.as_view(), name="face_detection"),
	path('object-detection', ObjectDetection.as_view(), name="object_detection"),
	path('image-classification', ImageClassification.as_view(), name="image_classification"),
	path('image-captioning', ImageCaptioning.as_view(), name="image_captioning"),
]