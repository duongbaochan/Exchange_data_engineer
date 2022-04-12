
"""
    Level 3 to level 1
"""

import Priority_Queue as PriQ
import Order
import csv

FileName = 'l3_data_v3.1.csv'
try:
    with open(FileName, "r") as File:
        print("Successfully opened ", FileName)

except FileNotFoundError:
    print("File cannot be found to read.")
except:
    print("Suspicious error.")


buy_q = PriQ.PriorityQueue()
sell_q = PriQ.PriorityQueue()

