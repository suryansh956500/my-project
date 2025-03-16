from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Function to translate text
def translate_text(text):
    t = GoogleTranslator(source='en', target='hi')
    return t.translate(text)

# Function to convert text to speech
def text_to_speech(text, file_name="speech.mp3"):
    tts = gTTS(text=text, lang='hi')
    tts.save(file_name)
    os.system("start " + file_name)  # 'start' for Windows, 'xdg-open' for Linux, 'open' for Mac

# Take input from the user
text = input("Please enter a text: ")

# Translate and convert to speech
translated = translate_text(text)
print("Translated Text:", translated)
