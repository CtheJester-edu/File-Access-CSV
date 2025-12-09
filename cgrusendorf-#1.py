"""
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

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
    current_date = datetime.strptime(row[0],'%Y-%m-%d')
    ohur = float(row[1])
    date.append(current_date)
    OHUR.append(ohur)



plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(date, OHUR, color='blue')
figure.autofmt_xdate()
graph.set_title('OHUR Numbers')
graph.set_ylabel('Unemployment Rate', fontsize=12)
plt.show()