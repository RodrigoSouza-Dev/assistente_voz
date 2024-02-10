#pip install SpeechRecognition
#pip install gtts
#pip install wikipedia
#pip install sounddevice

import speech_recognition as sr
from gtts import gTTS
import webbrowser
import subprocess
import sounddevice as sd
import numpy as np

def tts(texto, idioma="pt-br"):
    tts = gTTS(text=texto, lang=idioma)
    tts.save("audio.mp3")

def stt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = recognizer.listen(source)
    texto = recognizer.recognize_google(audio, language="pt-BR")
    return texto

def automatizar(comando):
    if "pesquisar wikipedia" in comando:
        termo = comando.split("pesquisar wikipedia")[1].strip()
        pesquisar_wikipedia(termo)
    elif "abrir youtube" in comando:
        webbrowser.open("https://www.youtube.com/")
    elif "farmácia mais próxima" in comando:
        webbrowser.open("https://www.google.com/maps/search/farmácia+mais+próxima")
    

def pesquisar_wikipedia(termo):
    try:
        result = wikipedia.summary(termo, sentences=2)
        print("Resultado da busca no Wikipedia:", result)
        tts(result)
    except Exception as e:
        print("Erro ao buscar informações no Wikipedia:", e)

while True:
    comando = stt().lower()
    print(f"Você disse: {comando}")

    if comando == "sair":
        break

    automatizar(comando)
