import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"

lang = 'en'

openai.api_key = api_key

guy = ""

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        try:
            r.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
            audio = r.listen(source)
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said

            if "Haami" in said:
                words = said.split()
                new_string = ' '.join(words[1:])
                print(new_string)
                completion = openai.Completion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": said}])
                text = completion.choices[0].message['content']
                speech = gTTS(text=text, lang=lang, slow=False)
                speech.save("welcome1.mp3")
                playsound.playsound("welcome1.mp3")

        except Exception as e:
            print("Exception:", e)

while True:
    if "stop" in guy:
        break

    get_audio()
