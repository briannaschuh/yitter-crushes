import sys
import pandas as pd
import csv
#import ipycytoscape
import networkx as nx

import edges
import numberAssignment

if __name__ == "__main__":
    
    #Make sure user gave the correct number of arguments
    if len(sys.argv) != 2:
        print("program.py [csv file of responses]")
        sys.exit(1)
        
    #Make sure the CSV file is in the same directory as this program
    file_name = str(sys.argv[1])
    if len(file_name) < 5:
        file_name += ".csv"
    else:
        if file_name[len(file_name) - 4: len(file_name)] != ".csv":
            file_name += ".csv"
    try:
        data = pd.read_csv(file_name)
    except:
        print("CSV file not found.")
        sys.exit(1)
    
    #Load the data
    with open(file_name) as f:
        data=[tuple(line) for line in csv.reader(f)]
    
    #Assign a unique number to each handle
    numbers_dict, total, response_list = numberAssignment.create_dict(data)
    print(numbers_dict)
    
    #Create edges of the directed graph
    edges_list = edges.create_edges(response_list, numbers_dict)
    
    #Write the CSV file
    file = open('arrows2.csv', 'w+', newline = '')
    with file:
        write = csv.writer(file)
        write.writerows(edges_list)
        