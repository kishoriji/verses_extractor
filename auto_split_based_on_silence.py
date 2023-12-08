from pydub import AudioSegment
from pydub.silence import detect_nonsilent


# def convert_time(str_time, offset):
#     parts = str_time.split(':')
#     m, s = map(int, parts[:2])
#     d = int(parts[2]) if len(parts) > 2 else 0
#     time_in_seconds = m * 60 + s + d / 10
#     return time_in_seconds + offset

def convert_time(str_time, offset):
    parts = str_time.split(':')
    h, m, s = [0] * 3
    if len(parts) == 3:
        h, m, s = map(int, parts)
    elif len(parts) == 2:
        m, s = map(int, parts)
    time_in_seconds = h * 3600 + m * 60 + s
    return time_in_seconds + offset


def split_audio(filepath, start_time, end_time):
    start_time = start_time * 1000
    end_time = end_time * 1000
    audio = AudioSegment.from_mp3(filepath)
    chunk = audio[start_time:end_time]

    # fine-tune the start and end times based on silence
    start_silence, end_silence = find_start_end_times(chunk)
    # print(start_time, start_silence, end_time, end_silence)
    fine_chunk = chunk[start_silence: end_silence]

    return fine_chunk


def find_start_end_times(audio_segment, min_silence_len=500, silence_thresh=-40):
    non_silent_ranges = detect_nonsilent(audio_segment, min_silence_len, silence_thresh)

    # ensure some non-silent ranges are found
    if non_silent_ranges:
        start_time = non_silent_ranges[0][0]
        end_time = non_silent_ranges[-1][1]
        return start_time, end_time

    # if no non-silent ranges found return None
    return None, None


def extract_audio(txt_filepath, audio_filepath, export_path):
    slokas = []
    with open(txt_filepath, 'r', encoding='utf-8') as file:
        # offset_line = file.readline()
        # offset = float(offset_line.strip())
        offset = 0
        for line in file.readlines():
            items = [item.strip() for item in line.strip().split(',')]
            if len(items) < 3:
                print(f'Skipping {items}')
                continue
            sloka_verse_no, start_time_str, end_time_str = items
            start_time, end_time = convert_time(start_time_str, offset), convert_time(end_time_str, offset)
            slokas.append((sloka_verse_no, start_time, end_time))
    sloka_counts = {}
    for sloka in slokas:
        sloka_verse_no, start_time, end_time = sloka
        print(sloka_verse_no, start_time, end_time)
        if sloka_verse_no not in sloka_counts:
            output_file = f"{export_path}/{sloka_verse_no}.mp3"
            sloka_counts[sloka_verse_no] = 1
        else:
            sloka_counts[sloka_verse_no] += 1
            output_file = f"{export_path}/{sloka_verse_no}_{sloka_counts[sloka_verse_no]}.mp3"
        chunk = split_audio(audio_filepath, start_time, end_time)
        chunk.export(output_file, format="mp3")


def main():
    name = 'Shruti Siddhant Saar/Shruti_Siddhant_Saar_4_12419'
    txt_filepath = f'slokas_location_in_lecture/{name}.txt'
    audio_filepath = f"/Users/kishoriji/sadhana/audio/{name}.mp3"
    export_path = f'slokas/{name}'
    extract_audio(txt_filepath, audio_filepath, export_path)


if __name__ == '__main__':
    main()
