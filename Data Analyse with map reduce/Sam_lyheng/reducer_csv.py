#!/usr/bin/env python

import sys

def reducer():
    max_temperatures = {}
    for line in sys.stdin:
        year, temperature = line.strip().split('\t')
        temperature = float(temperature)
        if year in max_temperatures:
            max_temperatures[year] = max(max_temperatures[year], temperature)
        else:
            max_temperatures[year] = temperature

    # Output maximum temperature for each year
    for year, max_temp in max_temperatures.items():
        print(f"{year}\t{max_temp}")

if __name__ == "__main__":
    reducer()
