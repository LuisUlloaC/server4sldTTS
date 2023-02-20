from django.urls import path
from .views import gTTs, download_file, b64

urlpatterns = [
    path('<language>/<text>/<filename>', gTTs),
    path('descargar/<str:filename>/', download_file),
    path('b64/<str:filename>/', b64),
]
