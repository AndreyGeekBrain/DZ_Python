PATH = 'name.txt'
phone_book = {}

def open_file():
    global phone_book, PATH
    with open(PATH,'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data,1):
        contact = contact.strip().split(';')
        phone_book[i] = contact
 
def save_file():
    global phone_book, PATH
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    print(data)
    data = '\n'.join(data)
    print(data)
    with open(PATH, 'w',encoding='UTF-8') as file:
        file.write(data)

