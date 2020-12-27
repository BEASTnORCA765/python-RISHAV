import speech_recognition as sr 
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
def speech_to_text(file):
    audio = sr.AudioFile(file)
    with audio as source:
        speech = sr.Recognizer().record(source)
        try:
            text = sr.Recognizer().recognize_google(speech,language ='en-us' )
            print(text)
        except:
            print("chal hat")
if __name__ == "__main__":
    address = r'C:\Users\subha\Downloads\Recording.Wav'
    speech_to_text(address)

        

