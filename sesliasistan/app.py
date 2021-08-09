from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os


r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        return voice

def response(voice):
    if 'Merhaba' in voice:
        speak("merhaba")
    if 'Sen kimsin' in voice:
        speak('ben senin sesli asistanınım')
    if 'adın ne' in voice:
        speak('Marry')
    if 'nasılsın' in voice:
        speak('iyiyim sen nasılsın')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'teşekkür ederim' in voice:
        speak("rica ederim")
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
    if 'müzik ara' in voice:
        search = record('ne dinlemek istiyorsun')
        url = 'https://open.spotify.com/search/' + search
        webbrowser.get().open(url)
        speak(search + 'keyfini çıkar')
    if 'steamde ara' in voice:
        search = record('hangi oyuna bakmak istiyorsun')
        url = 'https://store.steampowered.com/search/' + search
        webbrowser.get().open(url)
    if 'youtubede ara' in voice:
        search = record('ne aramak istiyorsun')
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
    if 'netflixte ara' in voice:
        search = record('ne aramak istiyorsun')
        url = 'https://www.netflix.com/search?q=' + search
        webbrowser.get().open(url)
    if 'kapat' in voice:
        speak('görüşürüz')
        exit()

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Nasıl yardımcı olabilirim')
while True:
    voice = record()
    print(voice)
    response(voice)
