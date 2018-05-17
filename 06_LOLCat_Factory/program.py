import cat_service

"""
Important things to learn:
    In the function get_or_create_output_folder(), to create a cat_pictures
    folder, a base folder (os.path.dirname(__file)) is used instead of the
    current directory ('.'). It is because by using the base folder, the
    cat_pictures directory can always be created next to the program.py file.
    Consider this, if in the terminal, the working directory is not in that
    where program.py sits in, for example, in the home folder, then the
    cat_pictures folder will be created in the home folder.

    full_path = os.path.abspath(os.path.join('.', folder))

    will be replaced by:

    full_path = os.path.join(base_folder, folder)
"""
import os


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    # display cats


def print_header():
    print('--------------------------------------------------')
    print('                   LOLCat Factory')
    print('--------------------------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('Done')


if __name__ == '__main__':
    main()
