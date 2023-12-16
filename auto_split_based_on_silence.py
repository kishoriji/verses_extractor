import os

from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_nonsilent

from utils import convert_time


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


import subprocess


def git_diff_lines(filepath):
    # Get the output of git diff command as a string
    diff_output = subprocess.check_output(['git', 'diff', 'HEAD', filepath]).decode()

    changed_lines = []
    for line in diff_output.split('\n'):
        # Only new lines start with a '+', but skip the '+++' line
        if line.startswith('+') and not line.startswith('+++'):
            # Remove the '+' at the beginning and strip extra whitespaces
            changed_line = line[1:].strip()
            changed_lines.append(changed_line)

    return changed_lines


def get_all_lines(filepath):
    lines = []
    with open(filepath, encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def extract_audio(txt_filepath, audio_filepath, export_path):
    slokas = []

    # offset_line = file.readline()
    # offset = float(offset_line.strip())
    offset = 0
    lines = git_diff_lines(txt_filepath)
    #lines = get_all_lines(txt_filepath)
    print(f'processing {len(lines)} lines')
    for line in lines:
        print(line)
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
        play(chunk)
        chunk.export(output_file, format="mp3")


def main():
    name = 'brahm jeev maya/Brahm Jeev Maya Kya Hai 03 [aSekNB0qHSY]'
    txt_filepath = f'slokas_location_in_lecture/{name}.txt'
    audio_filepath = f"/Users/kishoriji/sadhana/audio/{name}.mp3"
    export_path = f'slokas/{name}'
    extract_audio(txt_filepath, audio_filepath, export_path)


if __name__ == '__main__':
    main()
