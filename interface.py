from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import Utilities.audio as audio_util
import subprocess
import librosa

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Audio Processor")
        master.geometry("500x400")

        # State variables
        self.audio_loaded = False
        self.audio_processed = False
        self.audio_playing = False

        self.file_path = None
        self.player_process = None


        self.frm = ttk.Frame(master, padding=25)
        self.frm.pack()

        self.label = ttk.Label(self.frm, text="Welcome to the Audio Processor")
        self.label.grid(row=0, column=0, columnspan=3)

        self.load_button = ttk.Button(self.frm, text="Load Audio", command=self.load_audio)
        self.load_button.grid(row=1, column=0)

        self.process_button = ttk.Button(self.frm, text="Process Audio", command=self.process_audio)
        self.process_button.grid(row=1, column=1)

        self.run_button = ttk.Button(self.frm, text="Run It!", command=self.play_lightshow)
        self.run_button.grid(row=1, column=2)

        self.status_label = ttk.Label(self.frm, text="Status: Waiting for audio")
        self.status_label.grid(row=2, column=0, columnspan=3)

    def load_audio(self):
        # Picking audio file by name
        # Only supporting mp3 in first version
        self.file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3")])
        
        if self.file_path:
            print(f"Selected file: {self.file_path}")

            # Placeholder for loading audio functionality
            self.audio_loaded = True
            self.status_label.config(text="Status: Audio Loaded")
        else:
            self.status_label.config(text="Status: No file selected")

    def process_audio(self):
        if not self.audio_loaded:
            self.status_label.config(text="Status: Please load audio first")
            return

        # Placeholder for processing audio functionality
        self.audio_processed = True
        self.status_label.config(text="Status: Ready to Play Lightshow")
    
    def play_lightshow(self):
        if not self.audio_loaded and self.audio_processed:
            self.status_label.config(text="Status: Please load and process audio first")
        
        if not self.audio_playing:
            self.audio_playing = True
            self.player_process = audio_util.play_audio(self.file_path)
            # Placeholder for playing lightshow functionality
            self.status_label.config(text="Status: Playing Lightshow")
            self.run_button.config(text="Stop Playback!")
        elif self.audio_playing:
            self.audio_playing = False
            audio_util.stop_audio(self.player_process)
            # Placeholder for stopping lightshow functionality
            self.status_label.config(text="Status: Ready to Play Lightshow")
            self.run_button.config(text="Run It!")
        