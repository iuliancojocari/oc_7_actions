import csv

MAX_INVEST = 500 * 100


def get_csv_data():
    """
    Get data from csv file

    :return: list of tuples
    """
    with open("data\\optimized.csv", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)

        for row in csv_reader:

            stock_name = row[0]

            # convert price from € to cents
            price_in_cents = float(row[1]) * 100

            # calculate benefit in cents
            benefit_in_cents = float(row[2]) * 100

            if price_in_cents <= 0 or benefit_in_cents <= 0:
                continue

            yield (stock_name, int(price_in_cents), int(benefit_in_cents))


def knap_sack(max_invest, actions):
    """
    Knapsack algorithm

    :param max_invest: Customer budget
    :param stocks: List of stocks

    :returns: Best combination of stocks
    """
    profit = [v[2] for v in actions]
    cost = [w[1] for w in actions]
    total_actions = len(profit)

    matrix = [[0 for x in range(max_invest + 1)] for x in range(total_actions + 1)]

    # Build table K[][] in bottom up manner
    for i in range(total_actions + 1):
        for w in range(max_invest + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif cost[i - 1] <= w:

                matrix[i][w] = max(
                    profit[i - 1] + matrix[i - 1][w - cost[i - 1]], matrix[i - 1][w]
                )

            else:
                matrix[i][w] = matrix[i - 1][w]

    best_combination = []
    while max_invest >= 0 and total_actions >= 0:

        if (
            matrix[total_actions][max_invest]
            == matrix[total_actions - 1][max_invest - cost[total_actions - 1]]
            + profit[total_actions - 1]
        ):

            best_combination.append(actions[total_actions - 1])
            max_invest -= cost[total_actions - 1]

        total_actions -= 1

    return best_combination


def display_results():
    """
    Display results
    """
    stocks = [stock for stock in get_csv_data()]
    best_combination = knap_sack(MAX_INVEST, stocks)

    print("Liste des actions achetées : \n")
    for stock in best_combination:
        print(f"{stock[0]} - {stock[1] / 100}€ - {stock[2] / 100}€")

    print(f"Total dépensé : {sum([stock[1] for stock in best_combination]) / 100}€")
    print(f"Profit total : {sum([stock[2] for stock in best_combination]) / 100}€")


if __name__ == "__main__":
    display_results()
