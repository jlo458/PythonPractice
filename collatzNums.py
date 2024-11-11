# This is a program finding all Collatz numbers up to 999, storing the results as a CSV file to put in excel later
# This was only made because my school network stopped me from accessing Matplotlib

import csv

def colSequence(n):
    num = n 
    count = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return num, count

csvFilePath = 'collatzNumbers.csv'

with open(csvFilePath, mode = "w", newline="") as file:
    writer = csv.writer(file)
    for n in range(1, 1000):
        data = colSequence(n)
        writer.writerow(data)
