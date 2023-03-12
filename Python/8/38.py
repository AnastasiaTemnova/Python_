#Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
#для изменения и удаления данных

def input_text():
    with open('file.txt', 'a') as data:
        data.write(input('Введите фамилию с заглавной буквы: '))
        data.write(' ')
        data.write(input('Введите имя с заглавной буквы: '))
        data.write(' ')
        data.write(input('Введите отчество с заглавной буквы: '))
        data.write(' ')
        data.write(input('Введите номер телефона в едином формате +7: '))
        data.write('\n')


def print_text():
    data = open('file.txt', 'r')
    print()
    for line in data:
        print(line)
    data.close()


def check_text(user_info):
    data = open('file.txt', 'r')
    for line in data.readlines():
        if user_info in line:
            print(line)
    data.close()


def change_all_coincidence(old, new):
    with open('file.txt', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(old, new)

    with open('file.txt', 'w') as f:
        f.write(new_data)



def delete_line(info):
    with open('file.txt') as data:
        list_del = []
        for line in data:
            if info in line:
                print(f'Данные по {line} удалены')
            else:
                list_del.append(line)
    with open('file.txt', 'w') as data:
        data.writelines(list_del)



match int(input('Если хотите добавить данные в телефонный справочник, введите 1; \n'
             'Если хотите вывести данные из телефонного справочника, введите 2; \n'
             'Если хотите произвести поиск по справочнику, введите 3; \n'
                'Если хотите заменить все совпадения по введеному тексту на новое, введите 4; \n'
                'Если хотите удалить строку, введите 5 ')):
    case 1:
        input_text()
    case 2:
        print_text()
    case 3:
        check_text(input('Введите данные '))
    case 4:
        change_all_coincidence(input('Введите текст, который хотите изменить '), input('Введите текст, на который хотите изменить '))
    case 5:
        delete_line(input('Введите строку, которую хотите удалить'))