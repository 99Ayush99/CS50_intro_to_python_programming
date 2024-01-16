import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
else:
    file_name, ext = sys.argv[1].split(".")
    if ext != "csv":
        sys.exit("Not a CSV file")
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader,headers="firstrow",tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")