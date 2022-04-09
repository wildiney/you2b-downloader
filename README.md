# YOU2B DOWNLOADER

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This script use youtube-dl to download a video from an given url

## How to use

### Docker

```shell
docker run --rm -it -v ${pwd}/downloads:/app_user/downloads --name youtubedl  youtubedl:latest
```

This command creates a download folder to share the downloaded file, so when asked, don't change the path. Just press enter.

### Your machine

Youtube-dl has to be in your path, if you are using Windows download the executable in <https://github.com/ytdl-org/youtube-dl#installation> or install using pip

```python
sudo -H pip install --upgrade youtube-dl
```

and then run:

```python
pip install -r requirements.txt
python app.py
```

Insert the folder path optionally, the video url and look at the file downloaded at the video folder

For Instagram, insert the page url, not the video url
