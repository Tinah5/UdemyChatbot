from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

YouTube_url = 'https://www.youtube.com/watch?v=5BKLjO_WvRk'

video_id = YouTube(YouTube_url).video_id

transcript = YouTubeTranscriptApi.get_transcript(video_id)

text_transcript = ''

for segment in transcript:
    text_transcript += segment['text'] + ' '

print(text_transcript)