import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-' * 40)
    print('           Journal App')
    print('-' * 40)


def run_event_loop():
    print('What do you want to do with your jounal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entris, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' or cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
    print('Done, GoodBye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your jounal entries: ")
    entries = reversed(data)
    for i, entry in enumerate(entries, 1):
        print('* [{}] {}'.format(i, entry))


def add_entries(data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
