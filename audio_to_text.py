import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile as wav
import queue
import os
#print(sd.query_devices())  # List available audio devices

def transcribe_audio(path_audio = "./data/recorded_audio.wav", #"./data/audio.mp3"
                     model_name = "large"):

    """ This function transcribe the audio to text

    Parameters:
        path_audio: str, path to the audio file
        model_name: str, the name of whisper transcription model
        
    Returns:
        text_audio: str, the text transcription of the audio"""
    
    #  You can also use "turbo", "small", "medium", "large"
    model = whisper.load_model(model_name)
        
    result = model.transcribe(path_audio)

    return result["text"]

if __name__=="__main__":
    # Grounth truth
    expected_res = """Oh, he has been away from New York—he has been all round the world. He doesn't know many people here, but he's very sociable,
    and he wants to know every one."""
    # Audio transcription
    result = transcribe_audio()
    print(result)
