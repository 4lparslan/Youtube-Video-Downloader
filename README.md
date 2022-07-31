# Youtube-Video-Downloader
Download playlist or specific videos.

### Install
```
git clone https://github.com/4lparslan/Youtube-Video-Downloader
cd Youtube-Video-Downloader
pip install pytube
```
### Usage
## -> You can download only one specific video
```
python youtube_video_downloader.py -o https://www.youtube.com/watch?v=hdT-o9VuqRM
```
## -> You can download a full playlist
```
python youtube_video_downloader.py -p https://www.youtube.com/playlist?list=PL2788304DC59DBEB4
```
## -> You can download a part of playlist
The following command is for downloading a playlist videos starting from the 5th one.
```
python youtube_video_downloader.py -sp https://www.youtube.com/playlist?list=PL2788304DC59DBEB4 5
```
The following command is for downloading between 5th and 8th videos.
```
python youtube_video_downloader.py -sp https://www.youtube.com/playlist?list=PL2788304DC59DBEB4 5 8
```
