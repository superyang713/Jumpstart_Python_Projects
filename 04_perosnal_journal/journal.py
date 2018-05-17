"""
This is the journal module.
"""
import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the hournal to load.
    :return: Anew journal data structure populated with the file data.
    """
    # TODO: populate from file if it exist.
    data = []
    filepath = get_full_filepath(name)

    if os.path.exists(filepath):
        with open(filepath) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filepath = get_full_filepath(name)
    print('.... saving to: {}'.format(filepath))

    with open(filepath, 'w') as fin:
        for entry in journal_data:
            fin.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)


def get_full_filepath(name):
    filepath = os.path.abspath(os.path.join('journals', name + '.jrl'))
    return filepath
