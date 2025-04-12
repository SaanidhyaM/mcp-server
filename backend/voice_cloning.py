import requests
from elevenlabs import stream
from elevenlabs.client import ElevenLabs

def clone_voice(text, voice_id, api_key, output_path="tests\\output_audio.mp3"):
    client = ElevenLabs(api_key=api_key)

    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2"
    )

    with open(output_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)
    
    print(f"Audio saved to {output_path}")


# Example usage
api_key = "sk_cf7c9625d24a03a8480d71614c0984b02f4bb4e94aa61747"
voice_id = "JYesEroFZfIV2tXHwRem"
text = "Hello, this is a cloned voice."
clone_voice(text, voice_id, api_key)
