import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile as wav
import queue
import os
#print(sd.query_devices())  # List available audio devices


model = whisper.load_model("turbo") # "small", "medium", "large"

path_audio = "./data/"

result = model.transcribe(os.path.join(path_audio,"audio.mp3"))
print(result["text"])