from pydub import AudioSegment
from pydub.playback import play


def convert_time(str_time):
    parts = str_time.split(':')
    m, s = map(int, parts[:2])
    d = int(parts[2]) if len(parts) > 2 else 0
    time_in_seconds = m * 60 + s + d / 10
    return time_in_seconds + 15


def split_audio(filepath, start_time, end_time):
    start_time = start_time * 1000
    end_time = end_time * 1000
    audio = AudioSegment.from_mp3(filepath)
    chunk = audio[start_time:end_time]
    return chunk


def extract_audio(txt_filepath, audio_filepath, export_path):
    slokas = []
    with open(txt_filepath, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            sloka_verse_no, start_time_str, end_time_str = [item.strip() for item in line.strip().split(',')]
            start_time, end_time = convert_time(start_time_str), convert_time(end_time_str)
            slokas.append((sloka_verse_no, start_time, end_time))
    sloka = slokas[3]
    sloka_verse_no, start_time, end_time = sloka
    print(sloka_verse_no, start_time, end_time)
    output_file = f"{export_path}/{sloka_verse_no}.mp3"
    chunk = split_audio(audio_filepath, start_time, end_time)
    #play(chunk)
    chunk.export(output_file, format="mp3")


if __name__ == '__main__':
    txt_filepath = 'slokas_location_in_lecture/Brahm Jeev Maya Kya Hai 15 [qCekFCGy4Ro].txt'
    audio_filepath = "/Users/akashmatterlabs/Downloads/translate/Brahm Jeev Maya Kya Hai 15 [qCekFCGy4Ro].mp3"
    export_path = 'slokas/Brahm Jeev Maya Kya Hai 15 [qCekFCGy4Ro]'
    extract_audio(txt_filepath, audio_filepath, export_path)
