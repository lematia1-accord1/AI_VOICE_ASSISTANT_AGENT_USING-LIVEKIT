# voice_assistant.py
class VoiceAssistant:
    def __init__(self, vad, stt, llm, tts, chat_ctx, fnc_ctx):
        self.vad = vad
        self.stt = stt
        self.llm = llm
        self.tts = tts
        self.chat_ctx = chat_ctx
        self.fnc_ctx = fnc_ctx
        self.room = None

    def start(self, room):
        self.room = room
        # Set up STT, TTS, VAD listeners etc.
        # Usually connects audio and loops listening
        # (Implementation depends on your actual use case)

    async def say(self, message, allow_interruptions=False):
        await self.tts.say(message, allow_interruptions=allow_interruptions)
