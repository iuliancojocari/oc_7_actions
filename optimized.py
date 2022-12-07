import csv

def get_csv_data():
    """ Get data from csv file

    @return: list of tuples
    """
    with open("data\\optimized.csv", newline='') as csv_file:
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

def knapSack(max_invest, cost, profit, total_actions, actions): 
    matrix = [[0 for x in range(max_invest + 1)] for x in range(total_actions + 1)]
    
    # Build table K[][] in bottom up manner 
    for i in range(total_actions + 1): 
        for w in range(max_invest + 1): 
            if i == 0 or w == 0: 
                matrix[i][w] = 0
            elif cost[i-1] <= w:
                 
                matrix[i][w] = max(profit[i-1] + matrix[i-1][w-cost[i-1]], matrix[i-1][w]) 
                                
                
            else: 
                matrix[i][w] = matrix[i-1][w] 
      
    best_combination = []
    while max_invest >= 0 and total_actions >= 0:

        if matrix[total_actions][max_invest] == \
            matrix[total_actions-1][max_invest - cost[total_actions-1]] + profit[total_actions-1]:

            best_combination.append(actions[total_actions - 1])
            max_invest -= cost[total_actions-1]

        total_actions -= 1

    return sum([float(c[1] / 100) for c in best_combination])
   

actions = get_csv_data()

profit = [v[2] for v in actions]  # profit
cost = [w[1] for w in actions] # cost
max_invest = 50000 # max invest
total_actions = len(profit) 
print(knapSack(max_invest, cost, profit, total_actions, actions))