import speech_recognition as sr
import subprocess
import pyttsx3
import webbrowser
import pywhatkit
import time
from datetime import datetime
import cv2
import threading
import pyautogui

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Setting female voice

voiceRecognizer = sr.Recognizer()

camera_open = False
running = True

def handle_command(command):
    def jarvis():
        response = 'Hi Sir, I am at your service today.'
        engine.say(response)
        engine.runAndWait()

    def get_time():
        current_time = datetime.now().strftime('%H:%M')
        response = f'The time is {current_time}, sir! What can I do for you today?'
        engine.say(response)
        engine.runAndWait()

    def search():
        search_term = command.split('search for ')[1]
        print(f"Search term: {search_term}")
        search_url = f'https://www.google.com/search?q={search_term}'
        response = f'Searching for {search_term} on Google.'
        engine.say(response)
        engine.runAndWait()
        webbrowser.open(search_url)

    def play_song():
        song = command.split('play ')[1]   
        response = f'Playing {song} on YouTube.'
        engine.say(response)
        engine.runAndWait()
        pywhatkit.playonyt(song)

    def pause_song():
        # song = command.split('play ')[1]
        response = f'Pausing on YouTube.'
        engine.say(response)
        engine.runAndWait()
        pyautogui.press('space')

    def open_camera_cmd():
        global camera_open
        response = 'Opening camera... sir!'
        engine.say(response)
        engine.runAndWait()
        camera_open = True
        threading.Thread(target=open_camera).start()

    def turn_off_camera_cmd():
        global camera_open
        response = 'Turning off camera sir.'
        engine.say(response)
        engine.runAndWait()
        camera_open = False

    def object_detection():
        response = 'Running object detection.'
        engine.say(response)
        engine.runAndWait()
        run_object_detection()

    def bye():
        global running
        response = 'Bye sir!'
        engine.say(response)
        engine.runAndWait()
        running = False

    # Define the dictionary to map commands to functions
    commands = {
        'jarvis': jarvis,
        'time': get_time,
        'search for': search,
        'play': play_song,
        'pause':pause_song,
        'open camera': open_camera_cmd,
        'turn on camera': open_camera_cmd,
        'photo': open_camera_cmd,
        'turn off camera': turn_off_camera_cmd,
        'camera off': turn_off_camera_cmd,
        'what object is it': object_detection,
        'bye': bye,
        'buy': bye
    }

    # Check and execute the command
    for key in commands:
        if key in command.lower():
            commands[key]()
            break
    else:
        print("Command not recognized.")

def get_audio():
    global running
    while running:
        with sr.Microphone() as source:
            print("Clearing background noises...please wait...")
            voiceRecognizer.adjust_for_ambient_noise(source)
            print("Speak something...")
            audio = voiceRecognizer.listen(source)

            try:
                # Recognizing the speech
                command = voiceRecognizer.recognize_google(audio, language='en-US')
                print(f"You said: {command}")
                handle_command(command)
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
    cv2.destroyAllWindows()

def run_object_detection():
    subprocess.call(['python', r'C:\Users\user\PythonAudio\Object_Recognition.py'])

# Run the function to listen and perform operations
get_audio()
