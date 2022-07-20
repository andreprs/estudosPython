from django.urls import path
from . import views  # o ponto referencia a própria pasta (nesse caso, blog)


urlpatterns = [
    path('', views.index)
]