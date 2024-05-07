import json
import os
from collections import defaultdict


def get_all_slokas(series_folder):
    digits = set([str(i) for i in range(10)])
    print(digits)
    slokas = defaultdict(list)
    for top_root, top_dirs, _ in os.walk(series_folder):
        for top_dir in top_dirs:
            for root, _, files in os.walk(os.path.join(top_root, top_dir)):
                files_path = [os.path.join(top_root, root, name) for name in files]
                for i, file in enumerate(files):
                    name = file[:-4]
                    if name[-1] in digits and name[-2] == '_':
                        name = name[:-2]
                    name = name.replace('भाग ', 'भाग. ')
                    slokas[name].append(files_path[i])
    with open('group.json', 'w', encoding='utf-8') as f:
        json.dump(slokas, f, ensure_ascii=False, indent=4)
    print(len(slokas))

if __name__ == '__main__':
    series_folder = 'slokas/brahm jeev maya'
    get_all_slokas(series_folder)
