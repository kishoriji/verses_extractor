import json
import os
import shutil
from collections import defaultdict

from pydub import AudioSegment
from pydub.playback import play

GROUP_NAMES = {
    'गीता': 'gita',
    'महाभारत': 'mahabharat',
    'ramayan': 'ramcharitmanas',
    'भ.र.सि.': 'bhakti_rasamrit_sindhu',
    'भाग.': 'bhagwat',
    'ब्र.सू.': 'brahm_sutra',
    'ब्रह्मबिन्दू.': 'brahm_bindu',
    'संन्यासोप.': 'sanyaso',
    'ईशा.': 'isha',
    'मुक्तिको.': 'muktiko',
    'कृष्णोप.': 'krihsno',
    'महोप.': 'maho',
    'बृहदा.': 'mundako',
    'नारदपरि.': 'naradaparivrajaka',
    'छानदोग्यों': 'chandogyo',
    'ब्रह्मविद्योप.': 'brahm_vidya',
    'राधो': 'radha',
    'केनो.': 'keno',
    'गो.उ.ता.उप.': 'gopal_uttar_tapini',
    'गो.पू.ता.उप.': 'gopal_purv_tapini',
    'प्रश्नो.': 'prashno',
    'तैत्तिरीयो.': 'taittiriyo',
    'श्वेता.': 'shweta',
    'कठोप.': 'katho',
    'मुण्डको.': 'mundako',
    'छान्दो.': 'chandogyo',
    'मैत्रायण्यु.': 'maitrainuy',
    'मुदगलो': 'mudgalo',
    'माण्डूक्य.': 'manduky',
    'त्रि.ता.उप.': 'tripad_vibhuti_mahanarayana',
    'योगशिखोप.': 'yogashikha',
    'शाट्यायनी.': 'shaatyayani',
    'ऐतरेयो.': 'aitareya',
    'सुबालो.': 'subalo',
    'कौषीतकि.': 'kausitaki',
    'वेद': 'ved',
    'अथर्ववेद': 'atharved',
    'ऋग्वेद': 'rigved',
    'पु.सू.': 'purush_sukth',
    'र.आ.ब्रा.': '',
    'ब्रह्मसंहिता': 'bhakti_rasamrit_sindhu',
    'ब्रसू.': 'brahm_sutra',
    'म.स्मृ.': 'manu_smriti',
    'पंचदशी': 'shankaracharya',
    'प्रबोधसुधाकर': 'shankaracharya',
    'शांकरभाष्य': 'shankaracharya',
    'शंकराचार्य': 'shankaracharya',
    'योगसूत्र': 'yog_sutra',
    'ना.प.': 'narad_panchratra',
    'प.पु.': 'padma_purana',
    'प.पु.उ.खं.': 'padma_purana_uttar_khand',
    'प.सं.': 'parmatm_sandarbh',
    'ना.पु.': 'narad_puran',
    'म.पु.': 'matsy_puran',
    'ब्र.वै.पु.': 'brahm_vaivart_puran',
    'स्क.पु.': 'skand_puran',
    'ना.भ.सू.': 'narad_bhakti_sutra',
}


def get_all_slokas(series_folder):
    digits = set([str(i) for i in range(10)])
    slokas = defaultdict(list)
    for top_root, top_dirs, _ in os.walk(series_folder):
        for top_dir in top_dirs:
            for root, _, files in os.walk(os.path.join(top_root, top_dir)):
                files_path = [os.path.join(root, name) for name in files]
                for i, file in enumerate(files):
                    name = file[:-4]
                    if name[-1] in digits and name[-2] == '_':
                        name = name[:-2]
                    name = name.replace('भाग ', 'भाग. ')
                    name = name.replace('मुंडकों ', 'मुंडको ')
                    name = name.replace('तैत्तिरीयो ', 'तैत्तिरीयो. ')
                    name = name.replace('तैत्तिरीय. ', 'तैत्तिरीयो. ')
                    name = name.replace('प्रश्नों ', 'प्रश्नो. ')
                    name = name.replace('कौषीतकि ', 'कौषीतकि. ')
                    name = name.replace('केनों ', 'केनो. ')
                    name = name.replace('केनो ', 'केनो. ')
                    name = name.replace('श्वेता ', 'श्वेता. ')
                    name = name.replace('शाट्यायनी ', 'शाट्यायनी. ')
                    name = name.replace('राधोपनिषत् ', 'राधो ')
                    name = name.replace('राधोपनिषद ', 'राधो ')
                    name = name.replace('छानदोग्यों ', 'छान्दो. ')
                    name = name.replace('प्रबोध सुधाकर ', 'प्रबोधसुधाकर ')
                    # name = name.replace(' ', ' ')
                    name = name.replace('बृहदारण्यको ', 'बृहदा. ')
                    name = name.replace('बृहदारनको ', 'बृहदा. ')
                    name = name.replace('मुंडको ', 'मुण्डको. ')
                    name = name.replace('मुंडकों ', 'मुण्डको. ')
                    name = name.replace('मुण्डको ', 'मुण्डको. ')
                    name = name.replace('कठो ', 'कठोप. ')
                    name = name.replace('कौशित ', 'कौषीतकि. ')
                    name = name.replace('कौषितकी. ', 'कौषीतकि. ')
                    name = name.replace('कौषितकी ', 'कौषीतकि. ')
                    name = name.replace('स्कन्द पुराण ', 'स्क.पु. ')
                    name = name.replace('स्कन्द ', 'स्क.पु. ')
                    name = name.replace('विष्णु ', 'वि.पु. ')
                    name = name.replace('ब्रह्म संहिता ', 'ब्रह्मसंहिता ')
                    name = name.replace('पद्म पुराण ', 'प.पु. ')
                    slokas[name].append(files_path[i])
    with open('group.json', 'w', encoding='utf-8') as f:
        json.dump(slokas, f, ensure_ascii=False, indent=4)
    print('total slokas: ', len(slokas))
    return slokas


def group_slokas(slokas):
    groups = defaultdict(dict)
    for k, v in slokas.items():
        parts = k.split(' ')
        key, verse_no = parts[0], ' '.join(parts[1:])
        if key in GROUP_NAMES:
            groups[key][verse_no] = sorted(v)
    for group, v in groups.items():
        filename = f'{group}json' if '.' in group else f'{group}.json'
        with open(f'sloka_groups/{filename}', 'w') as f:
            json.dump(v, f, ensure_ascii=False, indent=4)
            print(group, len(v))


def read_json(filepath) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)


def find_missing_slokas(txt_slokas: dict, mp3_slokas: dict):
    count = 0
    for verse_no in txt_slokas:
        if verse_no not in mp3_slokas:
            print(verse_no)
            count += 1
    print(f'Total missing verses: {count}')


def find_extra_slokas(txt_slokas: dict, mp3_slokas: dict):
    for verse_no in mp3_slokas:
        if verse_no not in txt_slokas:
            print(verse_no)


def get_file_sizes(mp3_slokas: dict, verse_no):
    sorted_by_size = []
    for file in mp3_slokas[verse_no]:
        stat = os.stat(file)
        size = int(stat.st_size / 1024)
        sorted_by_size.append((size, file))
    sorted_by_size.sort(key=lambda x: x[0], reverse=True)
    print(sorted_by_size)
    #shutil.copy(sorted_by_size[0][1], '/Users/kishoriji/sadhana/audio/slokas mp3/tmp')
    # for item in sorted_by_size:
    #     print(item)
    #     audio = AudioSegment.from_mp3(item[1])
    #     play(audio)
    #     text = input('Continue\n')
    #     if 'y' not in text:
    #         return


def get_skip_list():
    skip = set()
    for _, _, files in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3/bhagwat'):
        for line in files:
            sloka = line.strip().replace('.mp3', '')
            skip.add(sloka.split(' ')[-1])
    print(f'total slokas to skip: {len(skip)}')
    return skip


if __name__ == '__main__':
    # series_folder = 'slokas/brahm jeev maya'
    # slokas = get_all_slokas(series_folder)
    # group_slokas(slokas)
    txt_slokas = read_json('slokas_txt/bhagwat.json')
    mp3_slokas = read_json('sloka_groups/भाग.json')
    # find_missing_slokas(txt_slokas, mp3_slokas)
    verse_no = '३-१५-४३'
    get_file_sizes(mp3_slokas, verse_no)
    skip = get_skip_list()
    print(skip)
    # for verse_no in mp3_slokas:
    #     if verse_no not in skip:
    #         # print(verse_no)
    #         get_file_sizes(mp3_slokas, verse_no)
    #
    find_missing_slokas(txt_slokas, skip)
    # for key in txt_slokas.keys():
    #     print(key)
    # find_extra_slokas(txt_slokas, mp3_slokas)
