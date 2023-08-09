menu = [ "### Notes - Main menu:",
    "Show notes",
    "Find notes",
    "Read notes",
    "Save notes",
    "Create note",
    "Update note",
    "Delete note"
]

# Выход из программы
def close( saved: bool ) -> int:
    menu = [ "### Notes - Exit the program?" ]
    menu.append( "Exit" )
    if not saved:
        menu.append( "Save and Exit" )
    return get_comand( menu, end="Back" )

# Вывод на экран меню
def menu_show( menu: list ) -> int:
    if menu != []: print( "\n" + menu[ 0 ] )
    for i in range( 1, len ( menu ) ):
        print( f"{ i }. { menu[ i ] }" )

# Проверка команды
def check_comand( count: int, req: str, end: str ) -> int:
    while True:
        print( f"0. {end}" )
        comand = input( f"Enter the {req}: " )
        if comand.isdigit() and 0 <= ( comand := int( comand ) ) <= count:
            return comand
        else:
            print( "\n[!] Invalid command" )

# Запрос команды
def get_comand( lt: list, req: str = "command", end: str = "Exit" ) -> int:
    while True:
        menu_show( lt )
        return check_comand( len( lt ), req, end )

# Запрос ID
def get_ID( lt: list, req: str = "command", end: str = "Exit" ) -> int:
    while True:
        notes_show( lt )
        if len( lt ) == 0:
            return 0
        return check_comand( len( lt ), req, end )

# Запрос Даты
def get_date( mes: str ) -> str:
    while True:
        date_input = input( f"{mes}" )
        return date_input

# Создание заметки
def note_input( tm: int ) -> list:
    note, status = editor( tm=tm )
    if status:
        return note
    return []

# Редактирование
def editor( note: list = [ "", "" ], tm: int = 25 ) -> ( list, bool ):
    mes = [ "Enter new title:> ",
            "Enter new note :> " ]
    i = 0
    while i < len( mes ):
        print( f"\n0. Back" )
        for j in range(i):
            if j == 0:
                print( f"Title: \"{note[j]}\"" )
        temp = input( mes[i] )
        if i == 0 and len( temp ) > tm :
            print( f"[!] Title no more than { tm } characters" )
            temp = temp[ :tm ]
        if temp == "":
            if note[i] != "":
                i +=1
            continue
        if temp == "0":
            i -= 1
            if i == -1:
                return note, False
            continue
        note[ i ] = temp.strip()
        i += 1
    else:
        return note, True

# Радактироваие заметки
def note_edit( notes, id, tm: int = 25 ):
    note_show( notes, id )
    note, status = editor( note=[notes[ id ][0], notes[ id ][1]], tm=tm )
    if status:
        if note == [notes[ id ][0], notes[ id ][1]]:
            return note, False
        return note, True
    return note, False

# Вывод на экран всех заметок
def notes_show( notes: list ):
    if len( notes ) == 0:
        notes_none()
    else:
        print( "\nNotes List:" )
        for i in range( len( notes ) ):
            print( f"{ i + 1 }. { ' | '.join( notes[ i ] ) }" )

# Вывод на экран заметок после поиска
def fnotes_show( notes: list, fnotes: list ):
    if len( notes ) == 0:
        notes_none()
    else:
        print( "\nFind notes list:" )
        for i in range( len( notes ) ):
            if notes[i] in fnotes:
                print( f"{ i + 1 }. { ' | '.join( notes[ i ] ) }" )

# Вывод на экран заметки
def note_show( notes: list, id: int ):
    print( f"\n{ id + 1 }. { ' | '.join( notes[ id ] ) }" )


### Info messages

# Нет заметок
def notes_none():
    print( "\n[!] No notes" )

# Заметки сохранены
def notes_saved():
    print( "\n[+] Notes successfully saved" )

# Заметки прочитаны
def notes_readed():
    print( "\n[+] Notes successfully readed" )

# Заметка добавлена
def note_added():
    print( "\n[+] Added a new note" )

# Заметка добавлена
def note_updated():
    print( "\n[+] Note successfully updated" )

# Заметка удалена
def note_deleted( note: list ):
    print( "\n[+] Note successfully deleted" )
    print( f"-. {'; '.join( note ) }" )


# # For tests
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     from controller import main
#     main()

# TODO: Переписать функцию вывода на экран заметок
# TODO: Переписать функцию вывода на экран заметок после поиска
