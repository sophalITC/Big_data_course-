#!/usr/bin/env python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin)
    for row in reader:
        if len(row) == 4:  # Assuming CSV columns: year, month, day, temperature
            year, month, day, temperature = row
            
            print(f"{year}\t{temperature}")


if __name__ == "__main__":
    mapper()
