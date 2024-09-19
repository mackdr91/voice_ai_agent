import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

load_dotenv()

async def entrypoint(ctx: JobContext): # WorkerOptions
    intial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            'You are a customer support agent for Acme IT Solutions.'
            ' Your clientele is Speech therapist practices.'
            ' You are helpful, creative, clever, and very friendly.'
            'You interface with the customer via voice using LiveKit.'
            'You should be short and concise with your responses and avoid repeating yourself and using unpronounable punctuations.'
        )
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    assistant=VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        tts=openai.TTS(),
        llm=openai.LLM(),
        chat_ctx=intial_ctx
    )

    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hey, Welcome to Acme IT Solutions. How can I help you?")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))