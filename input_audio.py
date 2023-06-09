# input_audio.py
import numpy as np
import sounddevice as sd
import pvporcupine
import whisper
from ai_assistant import AIAssistant
from config import pvporcupine_api
import os
import soundfile as sf

assistant = AIAssistant()

porcupine = pvporcupine.create(keywords=['grapefruit', 'porcupine'], access_key=pvporcupine_api)

def get_next_audio_frame(indata, frames, time, status):
    """Callback function to capture audio from the microphone."""
    global porcupine
    global assistant

    if porcupine is None:
        return

    pcm = np.int16(indata[:, 0] * 32768)
    keyword_index = porcupine.process(pcm)
    if keyword_index == 0:  # 'grapefruit' detected
        print('Hotword Detected: grapefruit')
        assistant.activate()  # Activate the assistant
        # Save audio data to a file
        sf.write('output.wav', pcm, porcupine.sample_rate)
        # Convert audio to text using Whisper ASR
        result = assistant.whisper_model.transcribe('output.wav')
        text = result['text']
        print(f"Transcribed text: {text}")
        # Pass the transcribed text to the AI assistant
        assistant.answer(text)
        # Delete the audio file after use
        os.remove('output.wav')
    elif keyword_index == 1:  # 'porcupine' detected
        print('Hotword Detected: porcupine')
        print('Ending conversation...')
        assistant.deactivate()  # Deactivate the assistant
