'''
Julia Perrotta
jperrot3@binghamton.edu
Section # B57
Assignment #1
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many people are in a room and output the total number of
  introductions if each person introduces themselves to every other person 
  once

OUTPUT to monitor:
  introductions (int) - when each person introduces themselves to every other
  person once
INPUT from keyboard:
  person_count (int)

GIVEN: 
  HALF (int) - 2

FORMULA:
  (person_count * (person_count - 1)) / HALF
'''

# CONSTANTS
person_count = input()
HALF = 2

# This program outputs the total number of introductions possible if each
# person in a room introduces themselves to every other person in the room 
# once, given the number of people in the room
# must give valid input to receive valid output

def main():
  # Explain purpose of program to user
  print("This program will print out the total number of introductions possible " +
        "if each person introduces themselves to every other person in the room")
  
  # Ask user for number of people in room
  person_count_str = input('How many people are in the room?: ')
  

  # Convert str data to int
  person_count = int(person_count_str)

  # Use the formula to compute the result
  introductions = (person_count * (person_count - 1)) / HALF

  # Display labeled and formatted introduction count
  print("The total amount of introductions is", introductions)
  
if __name__ == '__main__':
  main()

