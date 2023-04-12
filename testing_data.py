from utils import get_data, get_filtred_data

def right_data():
    data = get_data()
    data = get_filtred_data(data)
    return data

# print(len(right_data()))