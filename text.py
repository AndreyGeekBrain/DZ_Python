menu = ['Главное меню','Открыть файл','Сохранить файл','Показать файл',
        'Создать контакт','Найти контакт','Изменить контакт','Удалить контакт','Выход']

input_menu = 'Выберети пункт меню'
input_menu_eror = f'Ввести нужно число в диапазоне от 1 до {len(menu)-1}'

load_successfull = 'Телефонная книга загруженна успешно!'
save_successfull = 'Телефонная книга сохранена успешно!'

empty_book_error = 'Телефонная книга пуста или не открыта'

input_contact = ['Введите имя нового контакта: ', 'Введите номер телефона: ', 'Введите комментарий: ']

input_search_word = 'Ведите ключевое слово для поиска: '

input_edit_contact_id = 'Введите ID контакта, который хотите изменить: '

input_del_contact_id = 'Введите ID контакта, который хотите удалить: '

input_edit_contact = ['Введите имя измененого контакта: ', 'Введите номер телефона измененого контакта: ', 'Введите комментарий измененого когтакта:']

exit_program = 'До свидания!'

operation = ['создан', 'изменен' , 'удален']

def new_action(name: str, operation: str) -> str:
    return f'Контакт {name} успешно {operation}!'

def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'


