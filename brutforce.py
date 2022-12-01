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


