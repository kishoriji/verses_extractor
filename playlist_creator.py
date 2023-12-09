import os


def create_playlist(name):
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


def create_playlists():
    for top_root, top_dirs, _ in os.walk('slokas_location_in_lecture'):
        for top_dir in top_dirs:
            for root, _, files in os.walk(os.path.join(top_root, top_dir)):
                for file in files:
                    name = file.split('.')[0]
                    path = os.path.join(top_dir, name)
                    create_playlist(path)


if __name__ == '__main__':
    # create_playlist('Shruti Siddhant Saar/Shruti_Siddhant_Saar_2_12417')
    create_playlists()
