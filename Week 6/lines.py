import sys

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
else:
    file_name, ext = sys.argv[1].split(".")
    if ext != "py":
        sys.exit("Not a Python file")
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
for each_line in lines:
    each_line = each_line.lstrip()
    if not (each_line.startswith("#") or each_line.strip()==""):
        count += 1
    else:
        continue
print(count)
