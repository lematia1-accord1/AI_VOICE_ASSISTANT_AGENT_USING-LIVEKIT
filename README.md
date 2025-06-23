Description:
This project is a real-time AI-powered voice assistant built with LiveKit Agents, which enables audio streaming, speech recognition, natural language understanding, and speech synthesis. The assistant communicates entirely via voice, processing audio input from users, generating intelligent responses using LLMs (like OpenAI), and responding through synthesized speech.

Key Features:
- Voice Input Recognition – Captures microphone audio in real-time and transcribes it using OpenAI Whisper (STT).

- LLM Integration – Uses OpenAI's language model to understand and generate intelligent responses based on context.

- Voice Output (TTS) – Responds with spoken answers using OpenAI’s Text-to-Speech.

- LiveKit Agents – Handles real-time streaming and interaction using the LiveKit framework.

- Command Execution – (Optional) Supports basic function calls or task execution using custom AssistantFnc logic.

- Asynchronous Processing – Built with asyncio to manage non-blocking audio handling and background processing.

Tech Stack:
Component	Tool/Library
Voice Streaming	LiveKit Agents
Speech-to-Text	OpenAI Whisper (via plugins)
Language Model	OpenAI GPT (via plugins)
Text-to-Speech	OpenAI TTS (via plugins)
Voice Activity Detection	Silero VAD Plugin
Language	Python 3.12
Environment	venv, .env for configs

Project Structure Overview:
AI_VOICE_ASSISTANT_AGENT/

├── main.py                  # Entrypoint that runs the LiveKit agent
├── api.py                   # Defines AssistantFnc: custom command logic
├── voice_assistant.py       # Handles VAD, STT, LLM, TTS, and audio responses
├── .env                     # Contains secret keys, tokens, etc.
├── requirements.txt         # Lists dependencies
├── venv/                    # Python virtual environment (ignored in Git)
└── .gitignore               # Git ignore rules
How It Works (Flow)
main.py connects the assistant to a LiveKit room.

The assistant listens using microphone input.

The input audio is passed to OpenAI’s STT.

Transcribed text is sent to OpenAI’s LLM for a response.

The response is converted to speech and played back.

The session continues asynchronously until stopped.

Use Cases:
AI-powered smart assistants (custom Alexa/Google Assistant)

Voice-based customer support

Real-time voice interaction bots

Embedded assistants in mobile/web apps



