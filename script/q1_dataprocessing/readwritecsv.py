# Read from csv File: color_srgb.csv
import csv
with open('color_srgb.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
# Write to csv File: output_colors.csv
with open('output_colors.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Magenta", 255, 0, 255])
    writer.writerow(["Yellow", 255, 255, 0])

with open('output_colors.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
