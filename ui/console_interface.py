def show_data(data):
    print(data)


def show_info():
    print("""Simple commands for using this app:"
"show-all                                   - to look at all notes"
"get <note id>                              - to get note with id \"note id\""
"add <title> <message>                      - to add new note"
"update <note id> <new title> <new message> - for edit exicting note"
"del <note id>                              - to delete note with id""")


def show_all(notes):
    for key, item in notes.items():
        print("{} {}".format(key, item))


def show_one(note):
    print(note)


def does_not_exist():
    print("Such note does not exist!")
