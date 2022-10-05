import pytube

link = input('Enter Youtube Video Url')
if "list" in link:
    p = pytube.Playlist(link)
    for video in p.videos:
        video.streams.get_highest_resolution().download()
else:
    yt = pytube.YouTube(link)
    yt.streams.get_highest_resolution().download()



print('downloaded',link)