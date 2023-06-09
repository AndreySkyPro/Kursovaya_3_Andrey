import json
from datetime import datetime


def get_data():
    """
    Функция для чтения файла json
    :return: Возвращает данные из файла в формате list
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtred_data(data):
    """
    Функция для сортировки полученных данных, получает из списка данные со статусом EXECUTED и имеющие счет отправления
    :param data: Данные полученные из файла json
    :return: Отсортированный список
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    data = [x for x in data if 'from' in x]
    return data


def get_last_values(data, count_value):
    """
    Фунция для сортировки по ключевому параметру date от более новых к старым
    :param data: Отсортированный согласно условий список (EXECUTED and from)
    :param count_value: значение в формате int для получения требуемого количества значений в списке операций
    :return: Отсортированный по датам список определенной длинны
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_value]


def get_formated_data(data):
    """
    Функция для вывода данных в требуемом формате, преобразует формат даты, шифрует данные для вывода согласно ТЗ
    :param data: Отсортированный по датам список определенной длинны
    :return: Список значений для вывода
    """
    formated_data = []
    for row in data:
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row['description']
        sender = row['from'].split()
        if sender[0] != 'Счет':
            from_bill = sender[-1]
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            if len(sender) == 3:
                from_info = ' '.join(sender[:2])
            else:
                from_info = sender[0]
        else:
            from_bill = sender[-1]
            from_bill = f'** {from_bill[-4:]}'
            from_info = ''.join(sender[0])
        recipient = row['to'].split()
        if recipient[0] != 'Счет':
            recipient_bill = recipient[-1]
            recipient_bill = f'{recipient_bill[:4]} {recipient_bill[4:6]}** **** {recipient_bill[-4:]}'
            if len(recipient) == 3:
                recipient_info = ' '.join(recipient[:2])
            else:
                recipient_info = recipient[0]
        else:
            recipient_bill = recipient[-1]
            recipient_bill = f'**{recipient_bill[-4:]}'
            recipient_info = ''.join(recipient[0])

        amount = row['operationAmount']['amount']
        name = row['operationAmount']['currency']['name']

        formated_data.append(f"""
{date} {description}
{from_info} {from_bill} -> {recipient_info} {recipient_bill}
{amount} {name}""")
    return formated_data
