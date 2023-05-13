import sounddevice as sd
from ai_assistant import AIAssistant
from input_audio import get_next_audio_frame, porcupine

try:
    # Initialize AI assistant
    try:
        assistant = AIAssistant()
    except Exception as e:
        print(f"Error initializing AI assistant: {e}")
    print('>>> start')
    assistant.generate_speech('start')
    with sd.InputStream(callback=get_next_audio_frame,
                        channels=1,
                        samplerate=porcupine.sample_rate,
                        dtype='int16',
                        blocksize=porcupine.frame_length):
        listen = "Listening... Press Ctrl+C to stop."
        print(listen)
        assistant.generate_speech(listen)
        while True:
            pass
finally:
    if porcupine is not None:
        porcupine.delete()
