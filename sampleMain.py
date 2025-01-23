import sys
from datetime import datetime
import pyttsx3
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import threading
import queue
import smtplib
import pyjokes

from mainWINDOW import Ui_Form


class VoiceAssistant(QWidget):
    def __init__(self):
        super(VoiceAssistant, self).__init__()
        self.engine = pyttsx3.init()
        self.tts_queue = queue.Queue()  # Create a queue for TTS requests
        self.speaking = threading.Event()  # Event to track if speaking
        self.initUI()
        self.start_tts_thread()  # Start the TTS thread

    def initUI(self):
        self.mainUI = Ui_Form()
        self.mainUI.setupUi(self)

        self.mainUI.pushButton_2.clicked.connect(self.close)

        self.mainUI.pushButton_3.clicked.connect(self.greeting)
        self.mainUI.pushButton_3.clicked.connect(self.introduce)

        self.mainUI.movie = QtGui.QMovie("../../Downloads/7215336eb5f63cb507d59dd5429be565.gif")
        self.mainUI.label_7.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.listen_movie = QtGui.QMovie("../../Pictures/project 1/png/6ba174bf48e9b6dc8d8bd19d13c9caa9.gif")

        self.start_main_thread()  # Start the main function in a separate thread

    def start_tts_thread(self):
        tts_thread = threading.Thread(target=self.process_tts_queue)
        tts_thread.daemon = True
        tts_thread.start()

    def process_tts_queue(self):
        while True:
            audio = self.tts_queue.get()
            self.speaking.set()  # Set speaking flag
            self.engine.say(audio)
            self.engine.runAndWait()
            self.speaking.clear()  # Clear speaking flag
            self.tts_queue.task_done()

    def speak(self, audio):
        self.tts_queue.put(audio)  # Add TTS requests to the queue

    def run_in_thread(self, func, *args):
        thread = threading.Thread(target=func, args=args)
        thread.start()

    def introduce(self):
        self.speak("I am your voice assistant. How can I help you?")

    def greeting(self):
        hour = datetime.now().hour

        if 6 <= hour < 12:
            self.speak("Good morning madam.")
        elif 12 <= hour < 18:
            self.speak("Good afternoon madam.")
        elif 18 <= hour < 24:
            self.speak("Good evening madam.")
        else:
            self.speak("Good night madam.")

    def time(self):
        current_time = datetime.now().strftime("%I:%M:%S")
        self.speak(current_time)

    def date(self):
        year = int(datetime.now().year)
        month = int(datetime.now().month)
        day = int(datetime.now().day)

        self.speak("The current date is: ")
        self.speak(str(day))
        self.speak(str(month))
        self.speak(str(year))


        

    def searchGoogle(self):
        self.speak("What should I search?")
        search = self.takeCommandMIC()
        if search:
            wb.open('http://www.google.com/search?q=' + search)

    def takeCommandMIC(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 4000  # Adjust this threshold as needed
            audio = r.listen(source)
            print("Recognizing...")
            try:
                query1 = r.recognize_google(audio, language="en-in")
                print(query1)
                return query1
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")
                self.speak("Sorry, I did not understand that. Please try again.")
                return None
            except sr.RequestError:
                print("Request error from Google Speech Recognition service.")
                self.speak("Request error from Google Speech Recognition service.")
                return None

    def main(self):
        while True:
            query = None
            while not query:
                if not self.speaking.is_set():  # Check if not speaking
                    query = self.takeCommandMIC()

            query = query.lower()

            if 'time' in query:
                self.time()
            elif 'date' in query:
                self.date()
            elif 'joke' in query:
                self.speak(pyjokes.get_joke())
            elif 'wikipedia' in query:
                self.speak("Searching on wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                self.speak(result)
            elif 'search' in query:
                self.searchGoogle()
            elif 'offline' in query:
                self.close()

    def start_main_thread(self):
        main_thread = threading.Thread(target=self.main)
        main_thread.daemon = True
        main_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = VoiceAssistant()
    ui.show()
    sys.exit(app.exec_())
