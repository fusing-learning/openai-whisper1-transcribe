# 7th June 2025
Created this while learning how to create transcription using OpenAI's API (Model: `whisper-1`). While referencing to OpenAI's [sample](https://platform.openai.com/docs/api-reference/audio/createTranscription), made a few modifications below:
- Let user input file directory each time the script is executed
- Added a few parameters: 
    - `response_format`: So that I can specify the output file to be in `srt format`
    - `timestamp_granularities`: So that the texts are grouped by segments
- Instead of printing the output texts, asked to export them into an `.srt` file instead

Next steps:
- To prompt a window for user to select the audio file, instead of pasting the directory of the file. More user-friendly this way
- Allow user to select the `response_format`. To do so, the output file format also needs to change dynamically.
- Currently OpenAI API can accept audio file up to 25MB only, so needs a way to manage it, eg if the selected audio file > 25MB, slice them automatically. This will probably be more challenging but worth trying to figure this out.