import asyncio
from dotenv import load_dotenv

from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.plugins import openai, silero
from voice_assistant import VoiceAssistant
from api import AssistantFnc

load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    chat_ctx = llm.ChatContext([
    {
        "role": "system",
        "content": (
            "You are a voice assistant created by LiveKit. "
            "You interface with users via voice only. "
            "Speak concisely and avoid unpronounceable punctuation."
        ),
    }
])


    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=chat_ctx,
        fnc_ctx=AssistantFnc(),
    )

    assistant.start(ctx.room)

    await assistant.say("Hey, how can I help you today?", allow_interruptions=True)

    # ✅ Keeps the job running
    await asyncio.Event().wait()

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
