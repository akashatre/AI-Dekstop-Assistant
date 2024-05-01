# Voice Assistant with Tkinter

This project is a simple voice assistant that uses Python to recognize voice commands, perform tasks, and interact with the user via text-to-speech. It has a graphical user interface (GUI) with Tkinter and includes functionalities like opening websites, playing music, checking the time, and more.

## Getting Started

To run this voice assistant, you need Python installed on your laptop and several additional packages. This section explains how to set up your environment and run the application.

### Required Packages

To ensure the voice assistant works properly, you need to install the following packages:

- **pyttsx3**: Text-to-speech functionality.
- **SpeechRecognition**: Speech-to-text processing.
- **Tkinter**: Built-in GUI library in Python (usually pre-installed).
- **webbrowser**: Opens URLs in the default browser.
- **os**: Interacts with the operating system.

### Installation Instructions

Follow these steps to set up the environment and run the voice assistant:

1. **Install Python**: Ensure Python is installed on your laptop. You can download and install it from [Python.org](https://www.python.org/downloads/).

2. **Install Required Packages**: Use pip to install the necessary packages:

   ```bash
   pip install pyttsx3 speech_recognition




### Get App Path  

Type in cmd :

**where (app-name)**

### Usage Instructions
Once the application is running, you'll see a simple Tkinter GUI with a "Listen" button. Click this button to start voice recognition. The voice assistant listens for various commands, including:

- **Opening Websites** : Commands like "open YouTube" or "open Wikipedia" will open the corresponding website in the default browser.
- **Playing Music: Use** :"play music" to play a specific music file. Ensure the path is correctly set in the script.
- **Checking the Time** : Ask "what's the time?" to get the current time.
- **Opening Applications** : Commands like "open Notepad" or "open Camera" will launch those applications.

### Customization Options
You can customize the voice assistant in various ways:

- **Music Path**: Modify the music_path variable to point to a specific music file on your system.
- **Additional Commands**: Add new voice commands by extending the handle_command function in the script.
- **Text-to-Speech Configuration**: Adjust text-to-speech parameters (like voice, rate, and volume) in the say function.
### License Information
This project is licensed under the MIT License. You are free to use, modify, and distribute the code provided you comply with the terms of this license.

### Contact Information
If you have any questions or need assistance, feel free to contact me at akashatre123@gmail.com .


