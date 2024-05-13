import os
import shutil

mapping = {
    '0': '०',
    '1': '१',
    '2': '२',
    '3': '३',
    '4': '४',
    '5': '५',
    '6': '६',
    '7': '७',
    '8': '८',
    '9': '९',
}


def gita_renamer(eng_name):
    hi_name = 'गीता '
    skipped = ''
    for ch in eng_name:
        if ch in mapping:
            hi_name += mapping[ch]
        elif ch == '_':
            hi_name += '-'
        else:
            skipped += ch
    if skipped:
        print(f'skipped chars are: {skipped}')
    return hi_name


def all_gita_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/tmp/interimn'):
        for file in files:
            name, ext = file.split('.')
            if ext != 'mp3':
                continue
            print(name)
            hi_name = gita_renamer(name) + f'.{ext}'
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/2/{hi_name}')


def all_rigveda_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/upanishads/rigveda'):
        for file in files:
            name, ext = file.split('.')
            if ext != 'mp3':
                continue
            print(name)
            new_name = (name.replace('ऋगवेद ', '').replace('ऋग्वेद ', '')
                        + f'.{ext}')
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/{new_name}')


if __name__ == '__main__':
    all_rigveda_renamer()
