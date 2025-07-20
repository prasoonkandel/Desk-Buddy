import tkinter as tk
import threading
import speech_recognition as sr
import webbrowser as brave
import pyttsx3
import time
import sounddevice as sd
import numpy as np

from back import answer

gap = time.sleep
bot = pyttsx3.init()
recognise = sr.Recognizer()

running = False


def record_audio(duration=5, fs=44100):
    print("Listening...", end='', flush=True)  # Print without newline
    audio = sd.rec(int(duration * fs), samplerate=fs,
                   channels=1, dtype='int16')
    sd.wait()
    print('\r' + ' ' * len("Listening...") + '\r',
          end='', flush=True)  # Clear the line
    return audio.flatten()


def voice_assistant():
    global running
    print("Hello, I am your desk buddy")
    bot.say("Hello, I am your desk buddy")
    bot.runAndWait()

    print("Say something (say 'bye' to exit)")

    while running:
        try:
            # Record 5 seconds of audio from mic (you can change duration)
            audio_np = record_audio(5)

            # Convert numpy array audio to AudioData for speech_recognition
            audio_data = sr.AudioData(audio_np.tobytes(), 44100, 2)

            commandIn = recognise.recognize_google(audio_data)
            command = commandIn.lower()
            print(f"{command}")
            url, message = answer(command)
            message = str(message).strip()
            print(message)
            bot.say(message)
            bot.say(".")
            bot.runAndWait()
            if url == "bye":
                running = False
            elif url is None:
                continue
            else:
                brave.open(url)

        except sr.UnknownValueError:
            print("Sorry, I can't catch that!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except Exception as e:
            print("Oops! Something went wrong:", e)

    start_button.config(text="Start Assistant",
                        bg="#4CAF50", activebackground="#45a049")


def toggle_assistant():
    global running
    if not running:
        running = True
        start_button.config(text="Stop Assistant",
                            bg="#ff3333", activebackground="#e53935")
        threading.Thread(target=voice_assistant, daemon=True).start()
    else:
        running = False
        start_button.config(text="Start Assistant",
                            bg="#30CD35", activebackground="#45a049")


root = tk.Tk()
root.title("Desk Buddy Assistant")
root.geometry("500x400")
root.configure(bg="#121212")  # dark background


title_label = tk.Label(
    root,
    text="Desk Buddy",
    font=("Montserrat", 32, "bold"),
    fg="#ffffff",
    bg="#121212"
)
title_label.pack(pady=40)


start_button = tk.Button(
    root,
    text="Start Assistant",
    command=toggle_assistant,
    font=("Montserrat", 20, "bold"),
    fg="white",
    bg="#30CD35",
    activebackground="#157c00",
    bd=0,
    relief="flat",
    padx=40,
    pady=20
)
start_button.pack(pady=40)

root.mainloop()
