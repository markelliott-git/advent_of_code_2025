import pandas


def main():
    input = pandas.read_csv('day_1_input.csv')['instruction'].to_list()

    print(input)
if __name__ == "__main__":
    main()
