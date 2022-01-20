from django.urls import path
from . import views


urlpatterns = [
    path('', views.texto_a_audio, name='homepage'),
]
