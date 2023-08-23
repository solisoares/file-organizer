import os
from pathlib import Path

import filetype

AUDIO_EXT = ['.mp3']
VIDEO_EXT = ['.mp4', '.mkv', '.avi']
DOCUMENT_EXT = ['.pdf', '.docx', '.pptx', '.xls', '.doc', '.ppt', '.txt']
IMAGE_EXT = ['.jpg', '.jpeg', '.png']


def get_file_extension(file: str) -> str:
    """Returns the extension of a given file."""
    return Path(file).suffix.lower()


def organize_files(path: str) -> None:
    """Organizes files in a given directory into corresponding subdirectories based on file extension."""
    document_path = os.path.join(path, 'documents')
    images_path = os.path.join(path, 'images')
    audios_path = os.path.join(path, 'audios')
    videos_path = os.path.join(path, 'videos')
    others_path = os.path.join(path, 'others')

    # Check if subdirectories exist and create them if they don't
    for dir_path in [document_path, images_path, audios_path, videos_path, others_path]:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

    files = [file for file in os.listdir(path) if os.path.isfile(file)]

    for file_name in files:
        extension = get_file_extension(file_name)

        if not extension:
            try:
                extension = '.' + filetype.guess_extension(file_name)
            except TypeError:
                extension = ''

        if extension in IMAGE_EXT:
            new_path = os.path.join(images_path, file_name)
        elif extension in DOCUMENT_EXT:
            new_path = os.path.join(document_path, file_name)
        elif extension in VIDEO_EXT:
            new_path = os.path.join(videos_path, file_name)
        elif extension in AUDIO_EXT:
            new_path = os.path.join(audios_path, file_name)
        else:
            new_path = os.path.join(others_path, file_name)

        # Move the file to its corresponding folder
        os.rename(os.path.join(path, file_name), new_path)


if __name__ == '__main__':
    path = input(r'PATH: ')
    organize_files(path)
