import pandas

def main():
    input = pandas.read_csv('day_2_input.csv').columns.to_list()

    for range in input:
        print(range)

if __name__ == "__main__":
    main()
