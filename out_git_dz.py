# ДЗ Телефонный справочник

def main_menu():
    print('Добро пожаловать в телефонный справочник!\nВыберите пункт меню для работы:\n1. Просмотр содержимого телефонной книги\n2. Добавить контакт\n3. Отредактировать контакт\n4. Удалить контакт\n5. Выход')
    temp_input = int(input('Введите номер пункта меню: '))
    return temp_input

def menu_viseble_phonebook():
    print('Список абонентов телефонной книги:')
    with open('new.txt','r',encoding='UTF-8') as file:
        temp_list = file.readlines()
        for item in range(len(temp_list)):
            print(f'№_{item}: {temp_list[item]}')
        return temp_list

def menu_add_contact_phonebook():
     with open('new.txt','a',encoding='UTF-8') as file:
        str_contact = input("Введите данные абонента, через пробел (ФИО, телефон, комментарий к контакту):\n")
        file.write(str_contact + "\n")

def menu_change_contact_phonebook():
    temp_list = menu_viseble_phonebook()
    temp_nuber = int(input('Прошу для редактирования существующего контакта ввести номер(№) абонента из справочника выше:\n'))
    str_contact = input(f"Введите новые данные абонента №_{temp_nuber}, через пробел (ФИО, телефон, комментарий к контакту):\n")
    temp_list[temp_nuber] = str_contact+'\n'
    with open('new.txt','w',encoding='UTF-8') as file:
        file.writelines(temp_list)
    print(f'Контакт №_{temp_nuber} удален!')
    menu_viseble_phonebook()

def menu_del_contact_phonebook():
    list_1 = menu_viseble_phonebook()
    del_nuber = int(input('Прошу ввести номер(№) существующего абонента из справочника выше для удаления:\n'))
    list_1.pop(del_nuber)
    with open('new.txt','w',encoding='UTF-8') as file:
        file.writelines(list_1)
    print(f'Контакт №_{del_nuber} изменён!')
    menu_viseble_phonebook()

def menu_exit_phonebook(f1,f2):
    f1 = 0
    f2 = 0
    print('Вы вышли из программы!')

flag_global = True
while flag_global:
    in_menu = main_menu()
    flag_local = True
    while flag_local:
        if in_menu == 5:
            # menu_exit_phonebook(flag_global,flag_local)
            print('Вы вышли из программы!')
            flag_local = False
            flag_global = False
        if in_menu == 1:
            menu_viseble_phonebook()
            flag_local = False
        if in_menu == 2:
            menu_add_contact_phonebook()
            flag_local = False
        if in_menu == 3:
            menu_change_contact_phonebook()
            flag_local = False
        if in_menu == 4:
            menu_del_contact_phonebook()
            flag_local = False


