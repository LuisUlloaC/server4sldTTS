import base64
from datetime import datetime

import os
from django.http import JsonResponse, FileResponse, HttpResponse
from os import path
from rest_framework.status import  HTTP_404_NOT_FOUND

from .models import Audio
from .templatetags.gTTS import say

def_dir = os.getcwd()
dir_name = 'data'
temp_path = path.join(
    def_dir,
    path.join(
       'media',
        dir_name
    )
)


def gTTs(r, language='en', text='say it', filename=str(datetime.now)):
    """
    To return json dynamic TTS .mp3 link response :
    {mp3 : 'mp3 static link ...'}
    @param: language language to speak in (default: 'en')
    @param: text text to speak out (default: 'say it')
    """
    return JsonResponse(
        {'mp3':
        say(
            language=language,
            text=text,
            filename=filename
        ).replace('%5C', '/')}
    )


def download_file(request, filename):
    try:
        audio = Audio.objects.get(file_name=filename)
        return FileResponse(open( temp_path + '/' + str(audio) ,  'rb') )
    except Audio.DoesNotExist:
        return HTTP_404_NOT_FOUND
    
    
def b64(request , filename):
    try:
        audio = Audio.objects.get(file_name=filename)
        print(temp_path)
        print(audio)
        with open(temp_path + '/' + str(audio), 'rb') as bin_file:
            bin_data = bin_file.read()
            b64_encode = base64.b64encode(bin_data)
            print(str(HttpResponse(b64_encode)))
        return HttpResponse(b64_encode)
    except Audio.DoesNotExist:
        return HTTP_404_NOT_FOUND

