import csv
from itertools import combinations

def get_csv_data():
    """ Get data from csv file

    @return: list of tuples
    """
    with open("data\\brutforce.csv", newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        formated_data = []
        next(csv_reader)

        for row in csv_reader:
            stock_name = row[0]
            
            # convert price from € to cents
            price_in_cents = float(row[1]) * 100

            # calculate benefit in cents
            benefit_in_cents = float(row[2]) * 100
            
            # create tuple for each row with formated data
            formated_data.append((stock_name, int(price_in_cents), int(benefit_in_cents)))

        return formated_data


def generate_combinations(stocks):
    """ Generate all cominations with the given elements
    
    @param actions: list of tuples (tuple = stock)
    @return list: best stocks combinations
    """
    client_budget = 500 * 100
    profit = 0
    best_combination = []
    
    for i in range(len(stocks)):
        list_combinations = combinations(stocks, i+1)

        for combination in list_combinations:
            total_cost = calculate_cost(combination)

            if total_cost <= client_budget:
                total_profit = calculate_profit(combination)

                if total_profit > profit:
                    profit = total_profit
                    best_combination = combination
                    
    return best_combination

def calculate_profit(combination):
    """ Calculate the profit of all stocks of the combination
    @param combination: list of stocks
    @return int: all stocks profit
    """
    profit = []

    for stock in combination:
        profit.append(stock[2])

    return sum(profit)

def calculate_cost(combination):
    """ Calculate the cost of all stocks of the combination
    @param combination: list of stocks
    @return int: all stocks price
    """
    price = []

    for stock in combination:
        price.append(stock[1])

    return sum(price)

def display_result(best_combination):
    """ Display informations about the best combination

    @param best_combination: list of stocks
    """
    print("Liste des actions achetées :\n")

    for stock in best_combination:
        print(f"{stock[0]} {stock[1] / 100}€ {stock[2] / 100}€")

    print(f"\nSomme dépensée : {calculate_cost(best_combination) / 100}€")
    print(f"Profit total : {calculate_profit(best_combination) / 100}€")


if __name__ == "__main__":
    stocks = get_csv_data()
    best_combination = generate_combinations(stocks)
    display_result(best_combination)