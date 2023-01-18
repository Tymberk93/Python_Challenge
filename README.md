# Python_Challenge

###  #importing csv file.
import os

import csv

import pandas as pd

csvpath = "budget_data.csv"



###  #Reading csv file into Python
  with open ("budget_data.csv", "r") as csvfile:
  
    reader_variable = csv.reader(csvfile, delimiter=",")
    
    for row in reader_variable:
    
        print(row)
