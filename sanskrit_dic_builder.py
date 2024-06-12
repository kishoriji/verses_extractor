import collections
import json
import os


def definition_builder():
    with open('/Users/kishoriji/Downloads/apks/Movies/words.json') as f:
        data = json.load(f)
        words = {item["Id"]: item for item in data}
    valid_lang_ids = [3, 4, 5]
    dictionary = {}
    with open('/Users/kishoriji/Downloads/apks/Movies/definitions.json') as f:
        data = json.load(f)
        for item in data:
            if item['DictionarySourceId'] in valid_lang_ids:
                item_id = item['DictionaryRootId']
                if item_id not in words:
                    print(item_id)
                    continue
                word = words[item_id]['RootWord']
                word_eng = words[item_id]['RootWord_lipi']
                meaning = item['Meaning']
                dictionary[word] = meaning
    with open('sanskrit_dict.json', 'w', encoding='utf-8') as f:
        sorted_dict = collections.OrderedDict(sorted(dictionary.items()))
        json.dump(sorted_dict, f, ensure_ascii=False, indent=4)


def dhatus_processor():
    with open('dhatus.json') as f:
        data = json.load(f)
        dhatus = {}
        for item in data:
            dhatus[item['OriginalDhatu']] = {
                "hindi": item['MeaningHindi'],
                "english": item['MeaningEnglish'],
                'transliterate': item['OriginalDhatu_lipi']
            }
    with open('dhatus_dict.json', 'w', encoding='utf-8') as f:
        sorted_dict = collections.OrderedDict(sorted(dhatus.items()))
        json.dump(sorted_dict, f, ensure_ascii=False, indent=4)


def bhagwat_unarchiver():
    for root, _, files in os.walk('/Users/kishoriji/Downloads/apks/Movies/verses'):
        for file in files:
            print(file)


if __name__ == '__main__':
    # definition_builder()
    # dhatus_processor()
    bhagwat_unarchiver()
