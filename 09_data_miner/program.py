from research import Purchase
import os
import csv
import statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('--------------------------------------------------')
    print('                 Search File')
    print('--------------------------------------------------')


def get_data_file():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_folder, 'data',  'data.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
    return purchases


def query_data(data):
    # Before answer questinos, have to sort the data.
    data.sort(key=lambda x: x.price)

    # most expensive house:
    high_purchase = data[-1]
    print('the most expensive house is {:,} with {} beds and {} baths'.
          format(high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive house:
    low_purchase = data[0]
    print('the least expensive house is {:,} with {} beds and {} baths'.
          format(low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    average_price = statistics.mean([p.price for p in data])
    print('the average home price is {:,}'.format(int(average_price)))

    # average price for 2-bedroom house?
    two_bed_homes = [
        p  # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2
    ]
    ave_price = statistics.mean(
        [announce(p.price, 'price') for p in two_bed_homes[:5]]
    )
    ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print('the average 2bd home price is {:,}'.format(int(ave_price)))
    print('the average 2bd home area is {:,}'.format(int(ave_sqft)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
