import whisper

from config import model_config

def transcribe_whisper(file):
    model = whisper.load_model(model_config)
    result = model.transcribe(file, fp16=False)
    return result["text"]
