import os


def main():
    name = 'Shruti Siddhant Saar/Shruti_Siddhant_Saar_1_12416'
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


if __name__ == '__main__':
    main()
