import sys
from random import randint, random, randrange
from prettytable import PrettyTable
from references import *

def generate_input_string(start_string: str, options: list):
  input_string = start_string
  for i in range(len(options)):
    input_string += f"{i+1} for {options[i]}, "
  input_string = input_string[:-2] + ": "
  return input_string

def check_input(input: str, start: int, max: int):
  try:
    number = int(input)
    if number < start or number > max:
      raise ValueError
    return(number)
  except ValueError:
    print(f"Invalid input, please enter a number between {start} and {max}.")

def generate_table(table_type, minimum_tier, maximum_tier, table_size):
  table = PrettyTable()
  # table logic

  return table

def run_table():
  if __name__ == "__main__":
    if len(sys.argv) > 1:
      table_type_input = sys.argv[1]
    else:
      table_type_input = input(generate_input_string("Table type? ", ["Armor", "Consumables", "Items", "Weapons", "All of the above"]))
    table_type = check_input(table_type_input, 1, 5)
    if type(table_type) != int:
      return
    
    if len(sys.argv) > 2:
      minimum_tier_input = sys.argv[2]
    else:
      minimum_tier_input = input("Minimum tier? ")
    minimum_tier = check_input(minimum_tier_input, 1, 4)
    if type(minimum_tier) != int:
      return

    if len(sys.argv) > 3:
      maximum_tier_input = sys.argv[3]
    else:
      maximum_tier_input = input("Minimum tier? ")
    maximum_tier = check_input(maximum_tier_input, 1, 4)
    if type(maximum_tier) != int:
      return

    if minimum_tier > maximum_tier:
      print("Invalid input, minimum tier must be less than or equal ot maximum tier.")
      return

    if len(sys.argv) > 4:
      table_size_input = sys.argv[4]
    else:
      table_size_input = input(generate_input_string("Table size? ", ["Extra Small", "Small", "Medium", "Large", "Extra Large"]))
    table_size = check_input(table_size_input, 1, 5)
    if type(table_size) != int:
      return

    table = generate_table(table_type, minimum_tier, maximum_tier, table_size)
    print(table)

run_table()