"""
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt


path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
for index, col_title in enumerate(header_row):
    print(f'{index}, {col_title}', end=" ")

date = []
OHUR = []

for row in reader:
    time = (row[0])
    ohur = float(row[1])
    date.append(time)
    OHUR.append(ohur)



plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plt(OHUR, color='blue')
plt.show()