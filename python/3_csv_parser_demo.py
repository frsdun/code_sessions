# Parse csv

# Assumptions: only 'points.csv' not any csv, no error handling
# Goal: count number of columns, count points per name

# read in file
# split by line
# split by comma

with open('points.csv', 'r') as file:
    data = file.read()
    rows = data.split("\n")

    results = []

    for row in rows:
        values = row.split(",")
        results.append(values)
    
    headings = results[0]

    print("headings:", headings)
    print("number of headings:", len(headings))

    for row in results:
        if row[0] == "name":
            continue
        
        total = int(row[2]) + int(row[3]) + int(row[4])
        print(f"Total points for {row[0]} = {total}")



    