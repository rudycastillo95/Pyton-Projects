from youtube_transcript_api import YouTubeTranscriptApi

#In the below brackets, add the v = " " for any youtube video, e.g. https://www.youtube.com/watch?v=SCpgKvZB_VQ, from here add SCpgKvZB_VQ in the ("").
srt = YouTubeTranscriptApi.get_transcript("")

f = open("subtitles.txt", "w")

for i in srt:
    text = i['text']  #Just write f.write("{}\n".format(i)) to get whole transcript
    f.write(text)     
f.close()
