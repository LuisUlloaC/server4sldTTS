from datetime import datetime
from django.http import JsonResponse, FileResponse
from rest_framework.status import  HTTP_404_NOT_FOUND

from .models import Audio
from .templatetags.gTTS import say


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
        return FileResponse(open("media/"+ str(audio.path) + str(audio.file_name), "rb"))
    except Audio.DoesNotExist:
        return HTTP_404_NOT_FOUND


