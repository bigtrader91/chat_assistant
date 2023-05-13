# 🤖 AI Assistant with Raspberry Pi and GPT 🧠

This project is about creating an AI assistant using Raspberry Pi and GPT. The AI assistant remembers the conversation history using langchain, which slides the conversation content in a Windows format. The assistant takes voice input through a microphone, converts it to text using Whisper, and feeds it to GPT for generating responses. The responses are then converted back to voice for the user to hear.

## 📂 Project Structure
```
.
├── ai_assistant.py
├── config.py
├── input_audio.py
├── main.py
├── requirements.txt
```

## 🚀 Getting Started

1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the `requirements.txt` file.
3. Run the `main.py` script to start the AI assistant.

## 📚 How it Works

- `main.py`: This is the main script that initializes the AI assistant and listens for voice input.
- `input_audio.py`: This script captures audio from the microphone, detects hotwords, and transcribes the audio to text using Whisper ASR.
- `ai_assistant.py`: This script handles the conversation history, generates responses using GPT, and converts the responses to speech.
- `config.py`: This script contains the necessary configuration variables.

## 🎙️ Voice Commands

The AI assistant responds to the following voice commands:

- "grapefruit"
- "porcupine"

## 📖 Conversation History

The AI assistant uses a sliding window approach to remember the conversation history. It can remember up to the last 10 exchanges in the conversation.

## 📌 Note

This project is still under development. More features and improvements are coming soon!

## 📃 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

This project was made possible by the open-source community. Special thanks to OpenAI for the GPT model, Picovoice for the Porcupine wake word engine, and Eleven Labs for the text-to-speech service.
