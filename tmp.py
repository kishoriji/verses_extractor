# import os
#
# for root, _, files in os.walk('/Users/kishoriji/Downloads/whatsapp_backup'):
#     for file in files:
#         if file.startswith('AUD'):
#             src = f'{root}/{file}'
#             dest = f'{root}/{file}.mp3'
#             os.rename(src, dest)
#             print(file)
import json
import os
import shutil


def mp3_file_renamer(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.startswith('shayari_'):
                new_name = file.replace('shayari_', '')  # .replace('.mp3', ' ') + 'विवेक चूड़ामणि.mp3'
                src = f'{root}/{file}'
                dest = f'{root}/tmp/{new_name}'
                print(dest)
                shutil.copy(src, dest)


def process_stuti(filepath):
    alphabets = set([ch for ch in 'abcdefghijklmnopqrstuvwxyz'])
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            contains = False
            for ch in line:
                if ch in alphabets:
                    contains = True
                    break
            if not contains:
                if line.strip():
                    print(line.strip())


def build_json(text):
    terms = text.split(' ')
    kv = {key: "" for key in terms}
    print(json.dumps(kv, ensure_ascii=False))


import subprocess
import json


def get_playlist_info(playlist_url):
    command = ['yt-dlp', '--dump-json', '--flat-playlist', playlist_url]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return [json.loads(line) for line in result.stdout.splitlines()]


def get_video_size(video_url):
    command = ['yt-dlp', '-O', '%(filesize,filesize_approx)s', video_url]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    print(result)
    return int(result.stdout.strip())


def get_total_playlist_size(playlist_url):
    playlist_info = get_playlist_info(playlist_url)
    total_size = 0
    for video in playlist_info:
        video_url = video['url']
        size = get_video_size(video_url)
        total_size += size
    return total_size


def get_playlist_size():
    playlist_url = 'https://youtube.com/playlist?list=PLVCEar3Hj_7Mb0LTuMXHjNB3CkzqpcmJI&si=B2w2oPVd5JuqyIco'
    total_size = get_total_playlist_size(playlist_url)
    print(f'Total playlist size: {total_size}')
    print(f'Total playlist size: {total_size / (1024 * 1024):.2f} MB')


if __name__ == '__main__':
    # path = '/Users/kishoriji/sadhana/audio/slokas mp3/shayari'
    # mp3_file_renamer(path)
    # build_json("रे चित्त चिन्तय चिरं चरणौ मुरारेः पारं गमिष्यसि यतो भवसागरस्य । पुत्राः कलत्र मितरे न हि ते सहायाः सर्वं विलोकय सखे मृगतृष्णिकाभम्")
    # process_stuti('slokas_location_in_lecture/bhaj_govindam.txt')
    get_playlist_size()
