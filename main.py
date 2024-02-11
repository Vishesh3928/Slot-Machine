# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:03:35 2024

@author: vishesh
"""
"""learnings --
                syntax
                Using global variables
                for loops
                for else logic 
                nested list
                rows and columns
                
"""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
    }

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
    }

def check_winnings(columns, lines, bet , values):
    """
   Calculate the winnings based on the columns, lines, bet, and symbol values.
   Args:
       columns (list): The slot machine columns.
       lines (int): Number of lines to bet on.
       bet (int): Bet amount for each line.
       values (dict): Symbol values.
   Returns:
       tuple: A tuple containing the total winnings and the winning lines.
   """
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)
    return winnings, winnings_lines
 
def get_slot_machine_spin (rows , cols , symbol):
    """
    Generate a random spin of the slot machine.
    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary defining the count of each symbol.
    Returns:
        list: A list of columns representing the slot machine spin.
    """
    all_symbols = []
    for symbol , symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = [] 
    for col in range (cols):
            column=[]
            current_symbols = all_symbols[:]
            for row in range (rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            
            columns.append(column)
            
    return columns

def print_slot_machine(columns):
    """
   Print the slot machine spin.
   Args:
       columns (list): The slot machine columns.
   """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
        
def deposit():
    while True:
        amount= input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater tha 0.")
        else:
            print("please enter a number.")
    return amount
    
def get_number_of_lines():   # Prompt the user to enter the number of lines to bet on.
    
    while True:
        lines= input("Enter the number of lines you want to bet on (1-"+ str(MAX_LINES) + " )? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a vaild number of lines")
        else:
            print("please enter a number.")
    return lines

def get_bet():  # prompt the user to enter bet on each line
    while True:
        amount= input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if 1<= amount<= 100:
                break
            else:
                print(f"Must enter a valid bet amount between ${MIN_BET} - ${MAX_BET}." )
        else:
            print("please enter a number.")
    return amount
    

def spin(balance):   # performs one spin 
 
    lines = get_number_of_lines()
    while True:
         bet = get_bet()
         total_bet = bet * lines
         if total_bet > balance:
             print(f"your bet amount exceeds your balance. Current balance = ${balance} ")
         else:
           break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet} ")
   
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"you won ${winnings}.")
    print("you won on lines:", *winnings_lines)
    return winnings - total_bet 
    
def main():  
    """
    Main function to run the slot machine game.
    """
    
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to play ( q to quit)" )
        if answer == "q":
            break
        else:
            balance += spin(balance)
            if balance == 0:
                print("You are out of money. Please deposit more to continue playing.")
                answer = input("Press enter to make another deposit. (q to quit)")
                if answer == "q":
                    break
                balance = deposit()
     
    print(f"you left with ${balance}")
        
   
    
main()
            