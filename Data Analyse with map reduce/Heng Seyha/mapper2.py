import csv

# Open the CSV file in read mode
with open('weather_data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iteration through the rows in the csv file
    for row in csv_reader:
        print("{}\t{:.2f}".format(row[0], float(row[3])))