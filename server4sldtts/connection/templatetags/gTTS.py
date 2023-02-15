from django import template
from django.conf import settings
from django.templatetags.static import static
from gtts.tts import gTTS
from os import path, makedirs
import os
from sys import version_info
import shutil

from os.path import isfile
from ..models import Audio





# cur_dir = path.join(path.dirname(path.abspath(__file__)), '..')
def_dir = os.getcwd()
dir_name = 'data'
temp_path = path.join(
    def_dir,
    path.join(
       'media',
        dir_name
    )
)

register = template.Library()

@register.simple_tag
def say(
    language='en-us',
    text='Flask says Hi!',
    filename="file"):
    print(temp_path)
    for h, a in {'language': language, 'text': text}.items():
        if not isinstance(a, str):
            raise(TypeError("gTTS.say(%s) takes string" % h))
    try:
        ext_file = Audio.objects.get(text=text, language=language, filename=filename)
        if not isfile(path.join(temp_path, ext_file.file_name)):
            for file in Audio.objemediacts.filter(
                text=text, language=language, filename=filename).all():
                file.delete()
            ext_file = None
    except Exception:
        ext_file = None
    if not path.isdir(temp_path):
        makedirs(temp_path) if version_info.major == 2 else makedirs(
            temp_path, exist_ok=True
        )
    if ext_file is None:
        s = gTTS(text) if language == 'skip' else gTTS(
            text,
            lang=language)
        while True:
            fname = str(filename) + '.mp3'
            abp_fname = path.join(temp_path, fname)
            if not path.isfile(abp_fname):
                break
        Audio(text=text,
        language=language,
        file_name=fname).save()
        s.save(abp_fname)
    else:
        fname = ext_file.file_name
    return static('/'.join([dir_name, fname]))