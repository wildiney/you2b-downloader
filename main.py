import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')


def main():
    date = datetime.now()
    video_folder = os.environ.get('VIDEO_FOLDER')
    date_video = str(date.strftime("%Y")) + "-" + str(date.strftime("%m"))
    video_url = input("Insert the video url: ")

    os.system(
        'youtube-dl {0} -o {1}/{2}-%(title)s.%(ext)s'.format(video_url, video_folder, date_video))


if __name__ == '__main__':
    main()
