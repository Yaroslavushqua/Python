import sys
import view
import model 

def show_main_menu():
    while True:
        menu_num = view.start()
        if menu_num == '1': # показ работников
            result = model.all_employee()
            view.print_message(result)
        elif menu_num == '2': # добавление работника
            result2 = model.enter_contact_record()
            view.print_message(result2)
        elif menu_num == '3': # поиск работников
            data = view.insert_data('Поиск работника по фамилии:')
            result3 = model.search_employee_record(data)
            view.print_message(result3)
        elif menu_num == '4': # удаление работников
            data = view.insert_data('Поиск работника для удаления:')
            result4 = model.delete_contanct(data)
            view.print_message(result4)
        elif menu_num == '5': # выход из программы
        # break
            sys.exit
        else:
            print('Ошибка. Введите число от 1 до 4 \n')
            show_main_menu()