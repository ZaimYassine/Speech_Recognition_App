# speechbrain audio recognition model
from speechbrain.inference.ASR import EncoderDecoderASR


def transcribe_audio_speechbrain(path_audio = "./data/recorded_audio.wav"):

    """ This function transcribe the audio to text

    Parameters:
        path_audio: str, path to the audio file
        
    Returns:
        text_audio: str, the text transcription of the audio using speechbrain model"""
    
    asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-crdnn-rnnlm-librispeech")
    #asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-transformer-transformerlm-librispeech")
    
    result = asr_model.transcribe_file(path_audio)

    return result

if __name__ == "__main__":

    # Grounth truth
    expected_res = """Oh, he has been away from New York—he has been all round the world. He doesn't know many people here, but he's very sociable,
    and he wants to know every one."""

    path_audio = "./data/recorded_audio.wav" 
    path_audio2 = "./data/audio.mp3"

    # Audio transcription
    result = transcribe_audio_speechbrain(path_audio)
    result2 = transcribe_audio_speechbrain(path_audio2)

    print(result)
    print(result2)