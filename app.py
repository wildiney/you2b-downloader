import os
from datetime import datetime
from email.policy import default
import platform

import inquirer

from pathlib import Path


class GetVideoFromYoutube:
    def getVideoFolder(self):
        if platform.system() == 'Windows':
            default_path = str(Path.home()) + '\Videos'
        else:
            default_path = os.path.join(os.getcwd(), 'downloads')

        questions = [
            inquirer.Text(
                'folder',
                message='Select folder ',
                default=default_path
            )
        ]
        answers = inquirer.prompt(questions)
        if os.path.isdir(answers.get('folder')) == False:
            return False
        return '"' + answers.get('folder') + '"'

    def getVideoURL(self):
        questions = [inquirer.Text('videoURL', message='Insert youtube URL')]
        answers = inquirer.prompt(questions)
        return answers.get('videoURL')

    def title(self, title):
        print('')
        print('')
        print(''.center(80, '='))
        print(title.center(80, '='))
        print(''.center(80, '='))
        print('')

    def get(self, video_folder, video_url):
        date = datetime.now()
        date_video = str(date.strftime('%Y')) + '-' + str(date.strftime('%m'))

        if platform.system() == 'Windows':
            os.system(
                'youtube-dl {0} -o {1}/{2}-%(title)s.%(ext)s'.format(video_url, video_folder, date_video))
        else:
            os.system(
                "youtube-dl {0} -o /downloads/{1}-'%(title)s.%(ext)s'".format(video_url, date_video))


if __name__ == '__main__':
    getVideoFromYoutube = GetVideoFromYoutube()
    getVideoFromYoutube.title(' DOWNLOAD VIDEO FROM YOU2B ')
    while True:
        video_folder = getVideoFromYoutube.getVideoFolder()
        if video_folder == False:
            break

        video_url = getVideoFromYoutube.getVideoURL()
        if len(video_url) < 3:
            break

        getVideoFromYoutube.get(video_folder, video_url)

        if platform.system() != 'Windows':
            break
