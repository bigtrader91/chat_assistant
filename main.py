import sounddevice as sd
from ai_assistant import AIAssistant
from input_audio import get_next_audio_frame, porcupine

try:
    # Initialize AI assistant
    try:
        assistant = AIAssistant()
    except Exception as e:
        print(f"Error initializing AI assistant: {e}")
    print('>>>start')
    with sd.InputStream(callback=get_next_audio_frame,
                        channels=1,
                        samplerate=porcupine.sample_rate,
                        dtype='int16',
                        blocksize=porcupine.frame_length):
        print('Listening... Press Ctrl+C to stop.')
        while True:
            pass
finally:
    if porcupine is not None:
        porcupine.delete()
