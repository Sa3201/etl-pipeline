import csv

def extract_data(path='data/input.csv'):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    # this change is done to test feature extract step branch
    # this change is done to test feature extract step branch - 2nd
    return rows
