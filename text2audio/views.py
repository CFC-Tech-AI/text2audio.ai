from gtts import gTTS
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,"index.html")

@csrf_exempt
def text2audio(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            speech = gTTS(text)
            audio_buffer = BytesIO()
            speech.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            
            response = HttpResponse(audio_buffer.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="text_speech.mp3"'
            return response

    return render(request, 'text2audio.html')