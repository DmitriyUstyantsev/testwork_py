import model
import view


def main():
    notes = []
    notes = model.notes_read( notes, model.notes_fn )
    if notes != []:
        view.notes_show( notes )
        view.notes_readed()

    menu = view.menu.copy()
    while True:
        comand = view.get_comand( menu )
        args = []
        if   comand == 0: # Выход
            comand = view.close( model.notes_saved )
            if comand in [ 1, 2 ]:
                if comand == 2:
                    model.notes_save( notes, model.notes_fn )
                    view.notes_saved()
                exit()

        elif comand == 1: # Вывести все
            view.notes_show( notes )

        elif comand == 2: # Найти
            search_date = view.get_date( "Enter the date to search, format: yyyy.mm.dd:> " )
            fnotes = model.notes_find( notes, search_date )
            view.fnotes_show( notes, fnotes )

        elif comand == 3: # Чтение
            # fn = Запрос имени файла
            notes = model.notes_read( notes, model.notes_fn )
            view.notes_show( notes )

        elif comand == 4: # Запись
            if len( notes ) == 0:
                view.notes_none()
                continue
            # fn = Запрос имени файла
            model.notes_saved = model.notes_save( notes, model.notes_fn )
            if model.notes_saved:
                view.notes_saved()

        elif comand == 5: # Создать заметку
            note = view.note_input( model.note_title_max )
            if note != []:
                notes, model.notes_saved = model.note_new( notes, note )
                view.note_added()
            view.notes_show( notes )

        elif comand == 6: # Изменить заметку
            view.notes_show( notes )
            if len( notes ) == 0:
                continue
            id = view.check_comand( len( notes ), "note ID to update", "Back" )
            if id == 0:
                view.notes_show( notes )
                continue
            note, edited = view.note_edit( notes, id - 1, model.note_title_max )
            if edited:
                model.note_del( notes, id - 1 )
                notes, model.notes_saved = model.note_new( notes, note )
                view.note_updated()
            view.notes_show( notes )

        elif comand == 7: # Удалить заметку
            while True:
                id = view.get_ID( notes, "note ID to delete", "Back" )
                if id == 0:
                    break
                notes, note, model.notes_saved = model.note_del( notes, id - 1 )
                view.note_deleted( note )


# # For tests
# if __name__ == "__main__":
#     from os import system
#     system("cls")
#     main()
