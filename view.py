import text

# Функция, которая напечатает меню.
def main_menu():
    for i,item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choise = input(text.input_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.menu):
            return int(choise)
        else:
            print(text.input_menu_eror)

def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def show_book(book: dict[int, list[str]], msg: str):
    if book:
        print('\n' + '*' * 67)
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
        print('*' * 67 + '\n')
    else:
        print_message(msg)