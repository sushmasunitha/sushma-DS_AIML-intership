import csv


with open("students.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])