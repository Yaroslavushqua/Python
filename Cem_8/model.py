file_name = 'employee.csv'
file1 = open(file_name, 'a+')
file1.close()



def all_employee():
    with open(file_name, 'r+') as file:
        return file.readlines()

def search_employee_record(search_name):
    search_name = search_name.title()
    file1 = open(file_name, 'r+')
    file_contents = file1.readlines()
    found = False
    for line in file_contents:
        if search_name in line:
            return line
            found = True
            break
    if found == False:
        return 'Не найден'
        


def delete_contact(search_name):
    search_name = search_name.title()
    file1 = open(file_name, 'r+')
    file_contents = file1.readlines()

    found = False
    for line in file_contents:
        if search_name in line:
            print('Ваш контакт: ', end=' ')
            print(line)
            found = True
            file = open('employee.csv', 'r')
            f = file.read().replace(line, ' ')
            file2 = open('employee.csv', 'w')
            file2.write(f)
            file2.close()
            break
    if found == False:
        return 'Не найден'
        

def enter_contact_record():
    first = input('Введите имя: ')
    first = first.title()
    last = input('Введите фамилию: ')
    last = last.title()
    job = input('Введите должность: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите адрес электронной почты:')
    contact = ('[' + first + ' ' + last + '||' + job + '||' + phone + '||' + email +']\n')
    file1 = open(file_name, 'a+')
    file1.write(contact)
    file1.close()
    print('Работник\n ' + contact + 'успешно добавлен')
    