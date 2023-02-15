from shutil import rmtree
from os import path
from .templatetags.gTTS import temp_path
from .models import Audio


def remove_cache():
    """
    remove cache folder and Audio modal records
    """
    if path.isdir(temp_path):
        rmtree(temp_path)
    Audio.objects.all().delete()