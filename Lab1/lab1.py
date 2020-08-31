'''
Name Julia Perrotta
email jperrot3@binghamton.edu
Lab Section and CA Name A57 Owen Ifferte
Lab # 1
'''

## Do not write anything past column 78
## Go to next line instead (no wrapping!)
## USE MEANINGFUL NAMES!
## variables will use lower_snake_case
## constants will use UPPER_SNAKE_CASE

'''
ANALYSIS

RESTATE the problem clearly and without ambiguity

OUTPUT to monitor:
  out_variable_name1 (variable_type) - description (only when needed)
  out_variable_name2 (variable_type) - description
  . . .

INPUT from keyboard:
  (Note:  you can list converted variables here,
          rather than clutter the section with
          string versions that must be converted)
  in_variableName1 (variable_type) - description (only when needed)
  . . .

GIVENS (i.e., program constants):

  NAMED_CONSTANT1 (variable_type) - value
  NAMED_CONSTANT2 (variable_type) - value
  
  # Your code here:
  QUARTER (int) => 25


  
  TO_DOLLAR (int) => 100

PROCESSING:
  Get input, Convert str input to int values
  Find total value of each type of coin:  coin_type_value * coin_type_count
    (substitute actual coin_type:  quarter_value, quarter_count, etc.)
  Convert int value to dollar value (will be float):  total_value / 100
    (make 100 a named constant)
  Display output

  
'''

# CONSTANTS 
QUARTER = 25  # go ahead and code the remaining constants
DIME = 10
NICKEL = 5
PENNY = 1


## BRIEF description of overall program:
# This program outputs the total amount of change that a user has in dollars
# given the count of each type of coin

def main():
  ## START by giving the overall flow of your program in comments,
  ##   then interleave your code

  # Explain purpose of program to user
  print("This program will print out the total amount of change " +
        "you have in dollars when you provide a count of each type of coin")

  # Ask user for number of coins they have
  ## Start with quarters, end with pennies
  # Note constraints: no dollar, half-dollar coins
  quarter_count_str = input("Please enter the number of quarters you have: ")
  ## Input the rest here
  dime_count_str = input("Please enter the number of dimes you have: ")
  nickel_count_str = input("Please enter the number of nickels you have: ")
  penny_count_str = input("Please enter the number of pennies you have: ")
  

  # Convert str data to int
  quarter_count = int(quarter_count_str)
  ## Convert the rest here
  dime_count = int(dime_count_str)
  nickel_count = int(nickel_count_str)
  penny_count = int(penny_count_str)

  # Multiply the value of each type of coin by it's count and sum each result
  ## finish this: + (OTHER_COIN * OTHER_COIN_VALUE) . . .
  total_cents = (QUARTER * quarter_count) + (DIME * dime_count) + \
                (NICKEL * nickel_count) + (PENNY * penny_count)

  # Convert to dollars (float)
  # You can place dummy data here so your program will run initially
  total_dollars = float(total_cents) / 100.0

  # Display labeled and formatted amount in dollars
  print("The total amount of change you have in dollars is $%.2f" %
        total_dollars)
  

if __name__ == '__main__':
  main()
