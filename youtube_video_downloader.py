from pytube import YouTube 
from pytube import Playlist
import argparse
import os

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

#one video, playlist and splitted playlist arguments
group.add_argument('-o', type=str, help='Downloads only one video. Paste the URL of your video.')
group.add_argument('-p', type=str, help='Downloads a playlist. Paste the URL of your playlist.')
group.add_argument('-sp', type=str, nargs='+', help='Downloads a part of playlist. Paste the URL of your playlist and specify the first and last video number. You can specify only the starting number.')
group.add_argument('-ml', type=str, help='Download your own list from txt file.')
args = parser.parse_args()

#Creates a folder for downloaded video files
def downloader(video):
    path = r'Downloaded Youtube Videos'
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)

    video.download(path)


if args.o:
    url = args.o
    my_video = YouTube(url)
    print(my_video.title)
    print("Please wait...")
    my_video = my_video.streams.get_highest_resolution()
    downloader(my_video)
    print("Download successful.")

elif args.p:
    p = Playlist(args.p)
    print(f'Downloading: {p.title}')
    counter = 1
    total = len(p.videos)

    for video in p.videos:
        video.title = str(counter) + "- " + video.title
        print(str(counter) + "/" + str(total) + "  " + video.title)
        my_video = video.streams.get_highest_resolution()
        downloader(my_video)
        counter+=1
    
    print("Download successful.")

elif args.sp:
    p = Playlist(args.sp[0])
    print(f'Downloading: {p.title}')
    counter = 1
    total = len(p.videos)

    for video in p.videos:
        if(counter >= int(args.sp[1])) and (counter <= int(args.sp[2]) if len(args.sp)==3 else True):
            video.title = str(counter) + "- " + video.title
            print(str(counter) + "/" + str(total) + "  " + video.title)
            my_video = video.streams.get_highest_resolution()
            downloader(my_video)
        counter+=1
    
    print("Download successful.")

elif args.ml:
    path = args.ml
    abspath = os.path.abspath(path)
    
    # Using readlines()
    file = open(abspath, 'r')
    Lines = file.readlines()
    total = len(Lines)
      
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))

        the_video = YouTube(line)
        the_video = the_video.streams.get_highest_resolution()
        print(str(count) + "/" + str(total))
        downloader(the_video)
    print(str(count) + "file has been downloaded succesfully.")
