from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(f"""Title: {yt.title}
Views: {yt.views}""")

yd = yt.streams.get_highest_resolution()

yd.download('F:\one drive\OneDrive\Bureau')