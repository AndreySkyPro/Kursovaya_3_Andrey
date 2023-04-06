import json
from datetime import datetime

def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtred_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    data = [x for x in data if 'from' in x]
    return data

def get_last_values(data, count_value):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_value]

def get_formated_data(data):
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

        amount = row["amount"]
        name = row["name"]
        formated_data.append(f"""
{date} {description}
{from_info} {from_info} -> {recipient_info} {recipient_bill}
{amount} {name}
""")
    print(formated_data)


