import os
import time
import pyaudio
import speech_recognition as sr
import playsound 
from gtts import gTTS
import openai

api_key = "YOUR_KEY_HERE"

lang ='en'

openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                
                if "Saturn" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string) 
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    print(text)
                    
                    # Remove the file if it exists
                    if os.path.exists('welcome1.mp3'):
                        os.remove('welcome1.mp3')
                    
                    speech.save("welcome1.mp3")
                    time.sleep(1)  
                    playsound.playsound("welcome1.mp3")
                    
            except Exception:
                print("Standing by...")

        return said

    get_audio()
