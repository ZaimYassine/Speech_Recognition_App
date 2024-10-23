import streamlit as st
from st_audiorec import st_audiorec
from audio_to_text import transcribe_audio
import os
import scipy.io.wavfile as wav
from pydub import AudioSegment
from io import BytesIO

###################################
# Streamlit Audio recognition App
###################################
st.title("🦜🔗 Speech Recognition App")

#openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.info("Please load or record your audio!", icon="ℹ️")

selected_option = st.radio("Do you want load or record the Audio:", ('Record', 'Load'))

# Function to save the uploaded audio file and return its path
def save_uploaded_file(uploaded_file):
    ''' Save the uploaded file in the data folder'''
    save_path = os.path.join("./data/", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

# Function to read audio file into a NumPy array
def read_audio_file(file_path):
    audio_contain, sample_rate = sf.read(file_path)
    return audio_contain, sample_rate

def save_audio_file(audio_data, mp3 = False,
                    folder_path = "./data/",
                    file_name = "recorded_audio"):
    
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Add the extension of the file
    if mp3:
        file_name = file_name + ".mp3"
    else:
        file_name = file_name + ".wav"
    
    # Create the full path for the file
    file_path = os.path.join(folder_path, file_name)

    if mp3:
        # Convert audio bytes to an AudioSegment
        audio = AudioSegment.from_file(BytesIO(audio_data)) 

        # Export as MP3
        audio.export(file_path, format="mp3")

        print(f"MP3 file saved at: {file_path}")
        
        return file_path
    else:
        # Write the audio bytes to the file
        with open(file_path, "wb") as f:
            f.write(audio_data)
        
        print(f"File saved at: {file_path}")
        return file_path

audio_data = None
with st.form("audio_form"):

    if selected_option == 'Record':

        st.warning("Please record your audio!", icon="⚠")

        wav_audio_data = st_audiorec()

        if wav_audio_data is not None:
            st.audio(wav_audio_data, format='audio/wav')

            # Save the file in the specified folder
            file_path = save_audio_file(wav_audio_data)
            audio_data = file_path

    elif selected_option == 'Load':

        st.warning("Please load your audio!", icon="⚠")

        # Create a file uploader for audio files
        audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

        # If an audio file is uploaded
        if audio_file is not None:
            # Display the uploaded file name
            st.write("Playing audio:", audio_file.name)

            # Play the audio file
            st.audio(audio_file, format='audio/mp3')
                        
            audio_data = audio_file
            
            file_path = save_uploaded_file(audio_data)


    submitted = st.form_submit_button("Submit")

# import module which transcribe the audio and return the text
#text_audio = "This application aim to reconize the audio and sumarize it"

if submitted and audio_data is not None:
    #st.write(audio_data)
    #file_path = save_uploaded_file(audio_data)
    st.write(file_path)
    text_audio = transcribe_audio(path_audio = file_path)
    
    text = st.text_area("Audio to text:",
                        text_audio)