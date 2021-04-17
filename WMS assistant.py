import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
  def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")
    
    else:
        speak("Good Evening! Sir")

    speak("I am JARVIS. Please tell me, How may I help you ")
