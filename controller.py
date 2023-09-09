import model
import text
import view

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successfull)
            case 2:
                model.save_file()
                view.print_message(text.save_successfull)
            case 3:
                view.show_book(model.phone_book,text.empty_book_error)
            case 4:
                pass
            case 5:
                pass        
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass