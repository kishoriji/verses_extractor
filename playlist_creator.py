import os


def create_playlist_for_lecture(name):
    folder_path = os.path.abspath(f'slokas/{name}')  # get absolute path of the directory
    playlist_path = f"{folder_path}/playlist.m3u"

    with open(playlist_path, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            files = [os.path.join(root, name) for name in files]  # add directory path to filenames
            files = [os.path.abspath(name) for name in files]  # convert to absolute paths
            for name in sorted(files, key=os.path.getctime):
                name = os.path.relpath(name, start=folder_path)
                if name.endswith('.mp3'):
                    file.write(name + '\n')


def create_playlists_for_all_lecture():
    for top_root, top_dirs, _ in os.walk('slokas_location_in_lecture'):
        for top_dir in top_dirs:
            for root, _, files in os.walk(os.path.join(top_root, top_dir)):
                for file in files:
                    name = file.split('.')[0]
                    path = os.path.join(top_dir, name)
                    create_playlist_for_lecture(path)


def to_digit(text):
    try:
        return int(text)
    except:
        return text


def create_playlist_for_slokas(folder_path):
    name = folder_path.split('/')[-1].strip()
    playlist_path = f"{folder_path}/{name}.m3u"
    sorter = lambda x: [to_digit(dig) for dig in x.split('.')[0].split('_')]
    with open(playlist_path, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            files = [os.path.join(root, name) for name in files]  # add directory path to filenames
            files = [os.path.abspath(name) for name in files]  # convert to absolute paths
            for name in sorted(files, key=sorter):
                name = os.path.relpath(name, start=folder_path)
                if name.endswith('.mp3'):
                    file.write(name + '\n')
    old_playlist = f"{folder_path}/playlist.m3u"
    try:
        os.remove(old_playlist)
    except:
        pass


def create_playlists_for_all_slokas():
    for top_root, top_dirs, _ in os.walk('/Users/kishoriji/sadhana/audio/slokas mp3'):
        for top_dir in top_dirs:
            folder_path = os.path.join(top_root, top_dir)
            print(f'creating playlist for: {top_dir}')
            create_playlist_for_slokas(folder_path)


if __name__ == '__main__':
    # create_playlist_for_lecture('Radha Tattva/Radha Tatva 19-03-09')
    # create_playlists_for_lecture()
    #create_playlist_for_slokas('/Users/kishoriji/sadhana/audio/slokas mp3/brahm sutras')
    create_playlists_for_all_slokas()
