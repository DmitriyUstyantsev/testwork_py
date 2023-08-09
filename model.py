from csv import reader as csv_reader
from csv import writer as csv_writer
import datetime
from os.path import isfile


notes_fn = "notes"
notes_saved = True
note_title_max = 25


# Заметка - Создать
def note_new( notes: list, note: list ) -> ( list, bool ):
    saved = True
    note.append( datetime.datetime.now().strftime( "%Y.%m.%d %H:%M:%S" ) )
    if note not in notes:
        notes.append( note )
        saved = False
    return notes, saved

# Заметка - Обновить
def note_upd( notes: list, args: list ) -> list:
    num = args[0] - 1
    return notes

# Заметка - Удалить
def note_del( notes: list, id: int ) -> list:
    return notes, notes.pop( id ), False

# Заметки - Найти
def notes_find( notes: list, date: str ) -> list:
    f_notes = []
    for note in notes:
        add_date = datetime.datetime.strptime( note[2], '%Y.%m.%d %H:%M:%S')
        if add_date.strftime("%Y.%m.%d") == date:
            print( add_date.strftime("%Y.%m.%d"), date)
            f_notes.append(note)
    return f_notes

# Заметки - Сохранить
def notes_save( notes: list, file_name: str ) -> bool:
    file_path = f"{file_name}.csv"
    with open( file_path, "w", encoding="UTF-8", newline='' ) as fl:
        writer = csv_writer( fl, delimiter=";" )
        # writer.writerows(notes)
        for i in range( len( notes ) ):
            writer.writerow( notes[ i ] )
    return True

# Заметки - Загрузить
def notes_read( notes: list, file_name: str ) -> list:
    file_path = f"{file_name}.csv"
    if isfile( file_path ):
        with open( file_path, "r", encoding="UTF-8", newline='' ) as fl:
            reader = csv_reader( fl, delimiter=";" )
            for note in reader:
                if not ( note in notes ):
                    notes.append( note )
    return notes


# # For tests
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     from controller import main
#     main()
