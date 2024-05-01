import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import tkinter as tk


# Function to initialize text-to-speech
def init_speech():
    engine = pyttsx3.init()
    return engine


# Function to speak text
def say(engine, text):
    engine.say(text)
    engine.runAndWait()


# Function to capture voice commands
def take_command(engine):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise
        say(engine, "Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-IN')
            return query
        except sr.UnknownValueError:
            say(engine, "I couldn't understand. Please try again.")
            return ""
        except sr.RequestError:
            say(engine, "Network error. Please check your internet connection.")
            return ""


# Command handling function
def handle_command(engine, query):
    response = ""
    # List of websites to open based on commands
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.org"],
        ["google", "https://www.google.com"]
    ]

    # Check for commands to open websites
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            response = f"Opening {site[0]}..."
            webbrowser.open(site[1])

    # Command to play music
    if "play music" in query.lower():
        music_path =  "C:\\Users\\akash\\Downloads\\Zara-Zara-Bahekta-Hai-Mehekta-Hai(PagalWorld).mp3"
        if os.path.exists(music_path):
            response = "Playing music..."
            os.startfile(music_path)
        else:
            response = "Music file not found."

    # Command to get the current time
    elif "the time" in query.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The time is {current_time}"

    # Command to open Notepad
    elif "open notepad" in query.lower():
        response = "Opening Notepad..."
        os.startfile("C:\\Windows\\notepad.exe")

    # Command to open the camera
    elif "open camera" in query.lower():
        response = "Opening Camera..."
        os.system("start microsoft.windows.camera:")
        # os.startfile("C:\\Windows\\micwindows.camera:")

    return response


# Tkinter GUI setup
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Voice Assistant")

    # Initialize text-to-speech
    engine = init_speech()

    # Greet the user when the GUI starts
    say(engine, "Hey, I am Akki AI. How can I help you?")

    # Text box to display results
    text_box = tk.Text(root, height=6, width=50)
    text_box.pack()

    # Button to start voice recognition
    def on_listen():
        query = take_command(engine)
        if query:
            text_box.insert(tk.END, f"Command: {query}\n")
            response = handle_command(engine, query)
            say(engine, response)  # Voice response
            text_box.insert(tk.END, f"Response: {response}\n")

    # Create a listen button
    listen_button = tk.Button(root, text="Listen", command=on_listen)
    listen_button.pack()

    # Start the Tkinter event loop
    root.mainloop()


# Run the GUI
if __name__ == '__main__':
    create_gui()

