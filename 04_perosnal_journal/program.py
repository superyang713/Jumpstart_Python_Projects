
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
            list_entries()
        elif cmd == 'a':
            add_entries()
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))


def list_entries():
    print('list entries')


def add_entries():
    print('adding entries')


if __name__ == '__main__':
    main()
