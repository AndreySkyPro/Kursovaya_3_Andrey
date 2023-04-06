from utils import get_data, get_filtred_data, get_last_values, get_formated_data
def main():
    COUNT_VALUE = 50

    data = get_data()
    data = get_filtred_data(data)
    data = get_last_values(data, COUNT_VALUE)
    data = get_formated_data(data)
    print(data)



if __name__ == "__main__":
    main()

