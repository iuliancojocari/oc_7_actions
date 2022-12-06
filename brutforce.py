import os
import csv
from itertools import combinations

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
csv_brutforce = os.path.join(ROOT_DIR, "data\\optimized.csv")

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
            price_in_cents = float(row[1]) * 100

            # calculate benefit in cents
            benefit_in_cents = float(row[2]) * 100
            

            # create tuple for each row with formated data
            formated_data.append((action_name, int(price_in_cents), int(benefit_in_cents)))

        return formated_data


def generate_combinations(actions):
    client_budget = 500 * 100
    profit = 0
    best_combination = []
    
    for i in range(len(actions)):
        list_combinations = combinations(actions, i+1)

        for combination in list_combinations:
            total_cost = calculate_cost(combination)

            if total_cost <= client_budget:
                total_profit = calculate_profit(combination)

                if total_profit > profit:
                    profit = total_profit

                    best_combination = combination
                    
    return best_combination

def calculate_profit(combination):
    
    profit = []

    for action in combination:
        profit.append(action[2])

    return sum(profit)


def calculate_cost(combination):
    price = []

    for action in combination:
        price.append(action[1])

    return sum(price)

def display_result(best_combination):
    print("Liste des actions achetées :\n")

    for action in best_combination:
        print(f"{action[0]} {action[1] / 100}€ {action[2] / 100}€")

    print(f"\nSomme dépensée : {calculate_cost(best_combination) / 100}€")
    print(f"Profit total : {calculate_profit(best_combination) / 100}€")


if __name__ == "__main__":
    actions = get_csv_data(csv_brutforce)
    best_combination = generate_combinations(actions)
    display_result(best_combination)