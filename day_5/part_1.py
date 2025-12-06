import pandas


def main():

    ranges: list = pandas.read_csv('day_5_input_ranges.csv')['ranges'].to_list()
    ids: list = pandas.read_csv('day_5_input_ids.csv')['ids'].to_list()

    # print(ranges)
    print(ids)

if __name__ == "__main__":
    main()