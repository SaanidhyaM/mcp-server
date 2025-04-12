from elevenlabs.client import ElevenLabs
from error_handling import log_exception
import os

def clone_voice(text, voice_id, api_key, output_path="tests\\output_audio.mp3"):
    try:
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
        return output_path

    except Exception as e:
        log_exception(e, "Error during voice cloning")
        return None


