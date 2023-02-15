from django.urls import path
from .views import *

urlpatterns = [
    path('<language>/<text>/<filename>', gTTs),
    path('descargar/<str:filename>/', download_file),
]