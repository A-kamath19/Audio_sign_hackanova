from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name='home'),
    path("contactUs",views.contactUs,name ='contactUs'),
    path("text_to_speech",views.text_to_speech,name='text_to_speech'),
    path("speech_to_sign",views.speech_to_sign,name='speech_to_sign'),
    path("speech_to_letter", views.speech_to_letter, name='speech_to_letter'),
    path("text_to_sign",views.text_to_sign,name='text_to_sign'),
    path("list",views.list,name='list'),
    path("output",views.output,name='output'),
    path("frequent",views.frequent,name='frequent'),
]