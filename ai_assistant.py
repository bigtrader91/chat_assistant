import pickle

from elevenlabs import generate, play, set_api_key
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

from langchain.chat_models import ChatOpenAI
from langchain.memory.prompt import SUMMARY_PROMPT

from config import elevenlabs_api
import whisper

class AIAssistant:
    def __init__(self):
        self.conversation_with_summary = self.load_conversation()
        self.whisper_model = whisper.load_model('small')  # Load the Whisper model
        set_api_key(elevenlabs_api)

    def load_conversation(self):

        # Initialize a new conversation if no saved conversation exists.
        conversation_with_summary = ConversationChain(
            llm=ChatOpenAI(), 
            memory=ConversationBufferWindowMemory(k=10), 
            verbose=True
        )
        return conversation_with_summary

    def generate_speech(self, text: str):
        audio = generate(
            text=text,
            voice="Bella",
            model='eleven_multilingual_v1'
        )
        play(audio)

    def answer(self, query: str) -> str:
        # Try to generate the answer with GPT-4 based on the query.
        try:
            gpt_answer = self.conversation_with_summary.predict(input=query)
        except Exception as e:
            print(f"Error with GPT-4: {e}")
            gpt_answer = "I'm sorry, I couldn't generate an answer based on the search results."


        # Generate speech from the text answer.
        self.generate_speech(gpt_answer)

        return gpt_answer
