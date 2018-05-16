
def main():
    print_header()
    run_event_loop()


def print_header():
    print('-' * 40)
    print('           Journal App')
    print('-' * 40)


def run_event_loop():
    print('What do you want to do with your jounal?')
    cmd = None
    journal_data = []

    while cmd != 'x':
        cmd = input('[L]ist entris, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('Done, GoodBye!')


def list_entries(data):
    print("Your jounal entries: ")
    entries = reversed(data)
    for i, entry in enumerate(entries, 1):
        print('* [{}] {}'.format(i, entry))


def add_entries(data):
    text = input("Type your entry, <enter> to exit: ")
    data.append(text)


if __name__ == '__main__':
    main()
