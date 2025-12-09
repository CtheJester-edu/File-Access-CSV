"""
Unemployment Chart
Breaks down a two colum OHUR file on unemployment.
by Caleb Grusendorf
12/9/2025
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def CSV_extraction():

    """
    Function: Opens and resolves the header of the CSV file
    Inputs: None
    Outputs: CSV reader with the header resolved
    """
    path = Path('OHUR.csv')
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    #display check for testing purposes

    #print(header_row)
    #for index, col_title in enumerate(header_row):
       # print(f'{index}, {col_title}', end=" ")

    return reader

def csv_breakdown(reader):

    """
    Function: Breaks down the CSV file into its components
    Inputs: The reader for the CSV file after the header is resolved
    Outputs: The date and OHUR lists
    """

    date = []
    OHUR = []

    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        ohur = float(row[1])
        date.append(current_date)
        OHUR.append(ohur)
    return date,OHUR

def create_graph(date, OHUR):

    """
    Function: Sets up and draws the graph
    Inputs: Receives the dates and OHUR lists
    Outputs: Draws the graph to the screen
    """
    plt.style.use('dark_background')
    figure, graph = plt.subplots()

    graph.plot(date, OHUR, color='blue')
    figure.autofmt_xdate()
    graph.set_title('OHUR Numbers')
    graph.set_ylabel('Unemployment Rate', fontsize=12)
    graph.set_xlabel('Date')
    plt.show()

reader = CSV_extraction()
date, OHUR = csv_breakdown(reader)
create_graph(date, OHUR)