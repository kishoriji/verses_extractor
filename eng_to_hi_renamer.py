import os
import shutil
import urllib.parse

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

rev_mapping = {v: k for k, v in mapping.items()}


def gita_renamer_eng_to_hi(eng_name):
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


def gita_renamer_hi_to_eng(hi_name):
    eng_name = ''
    skipped = ''
    for ch in hi_name:
        if ch in rev_mapping:
            eng_name += rev_mapping[ch]
        elif ch == '-':
            eng_name += '_'
        else:
            skipped += ch
    if not eng_name:
        print(f'skipped chars are: {skipped}')
    return eng_name


def all_gita_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/gita'):
        for file in files:
            name, ext = file.split('.')
            if ext != 'mp3':
                continue
            print(name)
            eng_name = gita_renamer_hi_to_eng(name) + f'.{ext}'
            print(eng_name)
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/{eng_name}')


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


def bhagwat_rename_hi_to_en(hi_name):
    skipped = ''
    en_name = ''
    for ch in hi_name:
        if ch in rev_mapping:
            en_name += rev_mapping[ch]
        elif ch == '-':
            en_name += '_'
        else:
            skipped += ch
    if not en_name:
        print(f'skipped chars are: {skipped}')
    en_name.replace('भाग. ', '').replace('भाग ', '')
    return en_name.strip()


def all_bhagwat_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/bhagwat'):
        for file in files:
            if not file.endswith('.mp3'):
                continue
            name = file[:-4]
            print(name)
            eng_name = bhagwat_rename_hi_to_en(name) + '.mp3'
            print(eng_name)
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/{eng_name}')


def all_shwetashatar_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/upanishads/keno'):
        for file in files:
            if not file.endswith('.mp3'):
                continue
            name = file[:-4].replace('keno_', '') + '.mp3'
            print(name)
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/{name}')

def all_brahm_sutras_renamer():
    for root, dirs, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/brahma sutras'):
        for file in files:
            if not file.endswith('.mp3'):
                continue
            name = file[:-4]
            print(name)
            eng_name = gita_renamer_hi_to_eng(name) + '.mp3'
            print(eng_name)
            shutil.copy(f'{root}/{file}', f'/Users/kishoriji/sadhana/audio/slokas mp3/tmp/{eng_name}')


def playlist_processor():
    with open('slokas/playlists/sadhana.m3u', encoding='utf-8') as f:
        for line in f:
            if 'EXTINF' not in line:
                print(urllib.parse.unquote(line.strip()))

if __name__ == '__main__':
    #all_brahm_sutras_renamer()
    playlist_processor()
