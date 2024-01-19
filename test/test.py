import csv

data = [{'Name': 'John', 'Age': 25}, {'Name': 'Alice', 'Age': 30}]

# Concatenate values from all dictionaries into a single list
all_values = [value for row in data for value in row.values()]

# Open the CSV file in write mode
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write a single row with all concatenated values
    writer.writerow(all_values)
