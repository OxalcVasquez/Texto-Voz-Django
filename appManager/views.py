from django.shortcuts import render
from gtts import gTTS
import PyPDF4
import io

def texto_a_audio(request):
  idioma = 'es-us'
  audio = ''

  if request.method == 'POST':
    #    text = request.POST.get('text')
   if request.FILES.get('pdf'):
      pdf = request.FILES.get('pdf').read()
      # Si el pdf esta disponible

      if pdf:
          pdfReader = PyPDF4.PdfFileReader(io.BytesIO(pdf))
          contenido = ''
          # Creando un objeto por cada pagina
          for i in range(int(pdfReader.numPages)):
              contenido += pdfReader.getPage(i).extractText() + "\n"
          text = contenido
          audioGenerado = gTTS(text=text, lang=idioma, slow=False, )
          audioGenerado.save("static/speech.mp3")
          audio = 'ok'
          contexto = {
              'audio': audio,
          }
          return render(request, 'inicio.html', contexto)
   else:
      text = request.POST.get('text')
      audioGenerado = gTTS(text=text, lang=idioma, slow=False, )
      audioGenerado.save("static/speech.mp3")
      audio = 'ok'
      contexto = {
          'audio': audio,
      }
      return render(request, 'inicio.html', contexto)

  contexto = {
      'audio': audio,
  }
  return render(request, 'inicio.html', contexto)
