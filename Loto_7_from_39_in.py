import sys
import csv
import operator

def loto(list):
    with open("in.txt", 'r', newline='') as in_file:
        file = csv.reader(in_file, delimiter=' ')
        for row in file:
            hint = 0 
            for item in list:
                if item in row:
                    hint+=1
            if hint >= 3:
                print(f"Number of hints: {str(hint)} in combination: {str(row)}")

if __name__ == "__main__":
    print(f"Hello. Enter 7 numbers from 1 to 39 in format n1 n2 n3 n4 n5 n6 n7")
    combination = input("Enter combination: ")
    list = combination.split(' ')
    print(f"You entered: {list}")
    loto(list)