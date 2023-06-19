import speech_recognition as sr
import pyttsx3
import vlc
import os
import time


# Initialize the recongnizer
r = sr.Recognizer()

# function to convert text to speak
def Speaksong(command):

    # Indentatize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Infinitly loop for use to speak
while(1):

    # Exception handling to handle
    # Exception at the runtime 
    try:

        # use the microphone as source for input
        with sr.Microphone () as source2:
            # wait fir a second to let the recorgnizer
            # adjust the enrgy threshould based on 
            r.adjust_for_ambient_noise(source2, duration=0.2) 

            # Listens for the user's input
            audio2 = r.listen(source2)

            # using google to recorgnize audio2
            open = r.recognize_google(audio2)
            open = open.lower() 
            print("Did you say", open)
            Speaksong(open)
            if open == "Play First Song":
                print("Rdey to play Song")
                os.system("1.mp3")
                p = vlc.MediaPlayer("1.mp3")
            elif open == "Play Second Song":
                print("Rdey to play Song")
                os.system("2.mp3")
                p = vlc.MediaPlayer("2.mp3")
            elif open == "Play Third Song":
                print("Rdey to play Song")
                os.system("3.mp3")
                p = vlc.MediaPlayer("3.mp3")
            
    except sr.RequestError as e:
        print("Could not Request result :, {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")
