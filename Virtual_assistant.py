from __future__ import barry_as_FLUFL
from calendar import week, weekday
from pickle import TRUE
import pyttsx3 
import speech_recognition as sr
import datetime 
import wikipedia 
import webbrowser
import smtplib
import pyjokes 
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)
engine.setProperty('volume',15)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        
    else:
        speak("Good Evening!")  
      
    speak("I am ZAP. How may I help you?")  
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("I didnt get that....")  
        return "None"
    return query
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zapassistant99@gmail.com', 'bwffzuzgbfmhonyj')
    server.sendmail('zapassistant99@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'search on wikipedia about' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search on wikipedia about", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'how are you' in query:
            speak("I am fine.Hope you are well too!")  
            
        elif 'do you like me' in query:
            speak("NO!     lol just kidding you are a very nice person.")
            
        elif 'who created you' in query:
            speak("three cool guys yash ahad and samyak")
        
        elif 'tell me a joke' in query:
            jk = pyjokes.get_joke(language="en", category="neutral")
            speak(jk)
            
        elif 'open Youtube' in query:
            webbrowser.open("https://www.youtube.com/")
                
        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")   

        elif 'play music' in query:
            speak("Get ready to move")
            webbrowser.open("https://open.spotify.com/")

        elif 'show me the latest news' in query:
            speak('Here are some headlines from the Times of India,Happy reading!')
            news = webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            
        elif "what is today's day" in query:
             now = datetime.datetime.now()
             speak(f'Today is {now.strftime("%A")}')
             
        elif "what's the time" in query:
          now = datetime.datetime.now()
          speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

        elif 'send an email to yash' in query :
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashmahajan40@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the mail")    
        
        elif 'send an email to samyak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "samyakbputhran@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the mail")
                
        elif 'send an email to aahat khan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ahadk4170@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the mail")
                

        elif 'open calculator' in query:
                    r = sr.Recognizer()
                    my_mic_device = sr.Microphone(device_index=1)
                    with my_mic_device as source:
                     speak("Say what you want to calculate")
                    # r.adjust_for_ambient_noise(source)
                    # audio = r.listen(source)
                    my_string=takeCommand()
                    print(my_string)
                    def get_operator_fn(op):
                         return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'into' : operator.mul,
                            'divided' :operator.__truediv__,
                            'Mod' : operator.mod,
                            'mod' : operator.mod,
                            '^' : operator.xor,
                            }[op]
        
                    def eval_binary_expr(op1, oper, op2):
                            op1,op2 = int(op1), int(op2)
                            return get_operator_fn(oper)(op1, op2)
                            
                    speak(eval_binary_expr(*(my_string.split())))
          
                
                
        elif 'thank you' in query:    
            speak("Glad I can help!")    
            break
                
        
        
       


