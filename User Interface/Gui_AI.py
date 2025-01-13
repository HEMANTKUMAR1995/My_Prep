import speech_recognition as sr
import subprocess
import pyttsx3
import webbrowser
import pywhatkit
import time
from datetime import datetime
import cv2
import threading
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# Setting female voice - Make sure you select a valid voice index based on available voices
engine.setProperty("voice", voices[1].id)

voiceRecognizer = sr.Recognizer()

camera_open = False
running = True

# Create the main window
root = tk.Tk()
root.title("Voice Assistant with Object Detection")

# Create labels and buttons
label = Label(root, text="Voice Assistant")
label.pack()

start_button = Button(root, text="Start Camera", command=lambda: open_camera_ui())
start_button.pack()

stop_button = Button(root, text="Stop Camera", command=lambda: stop_camera_ui())
stop_button.pack()

exit_button = Button(root, text="Exit", command=lambda: exit_program())
exit_button.pack()

# Label to show camera feed
camera_label = Label(root)
camera_label.pack()

def open_camera_ui():
    global camera_open
    response = 'Opening camera... sir!'
    engine.say(response)
    engine.runAndWait()
    camera_open = True
    camera_thread = threading.Thread(target=open_camera)
    camera_thread.start()

def stop_camera_ui():
    global camera_open
    response = 'Turning off camera sir.'
    engine.say(response)
    engine.runAndWait()
    camera_open = False

def exit_program():
    global running
    response = 'Goodbye, sir!'
    engine.say(response)
    engine.runAndWait()
    running = False
    root.quit()

def get_audio():
    global camera_open, running
    with sr.Microphone() as source:
        print("Clearing background noises...please wait...")
        voiceRecognizer.adjust_for_ambient_noise(source)
        print("Speak something...")
        audio = voiceRecognizer.listen(source)

        try:
            # Recognizing the speech
            command = voiceRecognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            
            # Check for specific commands
            if 'jarvis' in command.lower():
                response = 'Hi Sir, I am at your service today.'
                engine.say(response)
                engine.runAndWait()
                
            elif 'how are you' in command.lower():
                response = 'I am fine, sir! What can I do for you today?'
                engine.say(response)
                engine.runAndWait()
                
            elif 'time' in command.lower():
                current_time = datetime.now().strftime('%H:%M')
                response = f'The time is {current_time}, sir! What can I do for you today?'
                engine.say(response)
                engine.runAndWait()
                
            elif 'chrome' in command.lower():
                response = 'Opening Google Chrome.'
                engine.say(response)
                engine.runAndWait()
                program = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                subprocess.call([program])

            elif 'youtube' in command.lower():
                response = 'Opening YouTube.'
                engine.say(response)
                engine.runAndWait()
                webbrowser.open('https://www.youtube.com/')
            
            elif 'search' in command.lower():   
                search_term = command.split('search for ')[1]
                print(f"Search term: {search_term}")
                search_url = f'https://www.google.com/search?q={search_term}'
                response = f'Searching for {search_term} on Google.'
                engine.say(response)
                engine.runAndWait()
                webbrowser.open(search_url)
            
            elif 'play' in command.lower():
                song = command.split('play ')[1]   
                response = f'Playing {song} on YouTube.'
                engine.say(response)
                engine.runAndWait()
                pywhatkit.playonyt(song)     
            
            elif 'open camera' in command.lower() or 'turn on camera' in command.lower() or 'photo' in command.lower():
                open_camera_ui()
            
            elif 'turn off camera' in command.lower() or 'camera off' in command.lower():
                stop_camera_ui()

            elif 'what object is it' in command.lower():
                response = 'Running object detection.'
                engine.say(response)
                engine.runAndWait()
                run_object_detection()
                
            elif 'bye' in command.lower():
                exit_program()

            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as ex:
            print(ex)

def open_camera():
    global camera_open
    cap = cv2.VideoCapture(0)
    while camera_open:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera_open = False
            break
    cap.release()

def run_object_detection():
    subprocess.call(['python', r'C:\Users\user\PythonAudio\Object_Recognition.py'])

# Run the function to listen and perform operations
def run_voice_assistant():
    while running:
        get_audio()
        time.sleep(1)

# Run the voice assistant in a separate thread
voice_assistant_thread = threading.Thread(target=run_voice_assistant)
voice_assistant_thread.start()

# Start the Tkinter main loop
root.mainloop()
