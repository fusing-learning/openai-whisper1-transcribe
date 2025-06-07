from openai import OpenAI
client = OpenAI()

audio_path = input("Enter audio file path: ")
audio_file = open(audio_path, "rb")

transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    response_format="srt",
    timestamp_granularities=["segment"]
)

output_path = audio_path.rsplit(".", 1)[0] + ".srt"
with open(output_path, "w", encoding="utf-8") as out_f:
    out_f.write(transcript)