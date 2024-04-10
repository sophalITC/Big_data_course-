import sys

# Initialize a dictionary to store temperature in each year
max_temp = {}

# Process input from the mapper
for line in sys.stdin:
    # Remove leading and trailing whitespaces and split the line on tabs
    line = line.strip()
    year, temp = line.split('\t')
    temp = float(temp)  

    if year in max_temp:
        max_temp[year].append(temp)
    else:
        max_temp[year] = [temp]

# Output max temp for exach year
for year in max_temp:
    print("{}\t{}".format(year, max(max_temp[year])))
