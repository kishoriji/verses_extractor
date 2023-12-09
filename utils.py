import os


def convert_time(str_time, offset=0):
    parts = str_time.split(':')
    h, m, s = [0] * 3
    if len(parts) == 3:
        h, m, s = map(float, parts)
    elif len(parts) == 2:
        m, s = map(float, parts)
    time_in_seconds = h * 3600 + m * 60 + s
    return time_in_seconds + offset


def check_time_increasing(txt_filepath):
    with open(txt_filepath, 'r', encoding='utf-8') as file:
        previous_start_time = 0
        for line in file.readlines():
            try:
                items = [item.strip() for item in line.strip().split(',')]
                if len(items) < 3:
                    print(f'Skipping {items}')
                    continue
                # print(len(items), items)
                sloka_verse_no, start_time_str, end_time_str = items
                start_time = convert_time(start_time_str)
                end_time = convert_time(end_time_str)
                if previous_start_time > start_time:
                    print(f'Previous start greater than current for verse {sloka_verse_no}')
                if start_time > end_time:
                    print(f'start greater than end for verse {sloka_verse_no}')
            except Exception as e:
                print(f'Error {line} {e}')


if __name__ == '__main__':
    for root, dirs, files in os.walk('slokas_location_in_lecture/Radha Tattva'):
        files = [os.path.join(root, name) for name in files]  # add directory path to filenames
        for file in files:
            print(file)
            check_time_increasing(file)
