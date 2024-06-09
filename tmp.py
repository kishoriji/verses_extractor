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


if __name__ == '__main__':
    # path = '/Users/kishoriji/sadhana/audio/slokas mp3/shayari'
    # mp3_file_renamer(path)
    build_json("रे चित्त चिन्तय चिरं चरणौ मुरारेः पारं गमिष्यसि यतो भवसागरस्य । पुत्राः कलत्र मितरे न हि ते सहायाः सर्वं विलोकय सखे मृगतृष्णिकाभम्")
    #process_stuti('slokas_location_in_lecture/bhaj_govindam.txt')
