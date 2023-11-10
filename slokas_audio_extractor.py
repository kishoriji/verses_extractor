from pydub import AudioSegment
from pydub.playback import play


def convert_time(str_time, offset):
    parts = str_time.split(':')
    m, s = map(int, parts[:2])
    d = int(parts[2]) if len(parts) > 2 else 0
    time_in_seconds = m * 60 + s + d / 10
    return time_in_seconds + offset
    # return time_in_seconds + 15


def split_audio(filepath, start_time, end_time):
    start_time = start_time * 1000
    end_time = end_time * 1000
    audio = AudioSegment.from_mp3(filepath)
    chunk = audio[start_time:end_time]
    return chunk


def extract_audio(txt_filepath, audio_filepath, export_path):
    slokas = []
    with open(txt_filepath, 'r', encoding='utf-8') as file:
        offset_line = file.readline()
        offset = float(offset_line.strip())
        for line in file.readlines():
            sloka_verse_no, start_time_str, end_time_str = [item.strip() for item in line.strip().split(',')]
            start_time, end_time = convert_time(start_time_str, offset), convert_time(end_time_str, offset)
            slokas.append((sloka_verse_no, start_time, end_time))
    sloka = slokas[11]
    sloka_verse_no, start_time, end_time = sloka
    print(sloka_verse_no, start_time, end_time)
    output_file = f"{export_path}/{sloka_verse_no}.mp3"
    chunk = split_audio(audio_filepath, start_time, end_time)
    play(chunk)
    chunk.export(output_file, format="mp3")


if __name__ == '__main__':
    name = 'Brahm Jeev Maya Kya Hai 16 [ei6Z8RaB2N0]'
    txt_filepath = f'slokas_location_in_lecture/{name}.txt'
    audio_filepath = f"/Users/akashmatterlabs/Downloads/translate/{name}.mp3"
    export_path = f'slokas/{name}'
    extract_audio(txt_filepath, audio_filepath, export_path)
