from utils import get_data, get_filtred_data, get_last_values
def main():
    data = get_data()
    data = get_filtred_data(data)
    data = get_last_values(data)
    print(data)



if __name__ == "__main__":
    main()

