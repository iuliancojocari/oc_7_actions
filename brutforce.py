from itertools import combinations
import os
import csv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

csv_brutforce = os.path.join(ROOT_DIR, "data\\brutforce.csv")

def get_csv_data(file):
    """ Get data from csv file
    :param file: file name
    :return: list of tuples
    """
    with open(file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        formated_data = []
        next(csv_reader)

        for row in csv_reader:
            action_name = row[0]

            # convert price from € to cents
            price_in_cents = int(row[1]) * 100

            # calculate benefit in cents
            benefit_in_percent = int(row[2]) / 100
            benefit_in_cents = price_in_cents * benefit_in_percent

            # create tuple for each row with formated data
            formated_data.append((action_name, price_in_cents, int(benefit_in_cents)))

        return formated_data


def combinations(actions):
    # customer price in cents (500€ * 100 cents)
    max_price = 500 * 100

    # sort actions list by benefit
    actions_sorted_list = sorted(actions, key=lambda action: action[2], reverse=True)
    
    combinations_list = []

    for action in actions_sorted_list:
        if action[1] < max_price:
            current_price = 0 if len(combinations_list) == 0 else sum([action[1] for action in combinations_list])

            if max_price > current_price + action[1]:
                combinations_list.append(action)
    
    return combinations_list


if __name__ == "__main__":
    actions = get_csv_data(csv_brutforce)
    combo = combinations(actions)

    for combination in combo:
        print(combination)

    total_price = sum([action[1] for action in combo]) / 100
    total_rent = sum([action[2] for action in combo]) / 100

    print(f"\nTotal price : {total_price}€")
    print(f"Total rent : {total_rent}€")
