import json

def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtred_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def get_last_values(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    for x in data:
        print(x['date'])

