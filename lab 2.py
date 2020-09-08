def q2():
  # 2 + (3 - 1) * 10 / 5 * (2 + 3)  # Start
  # 2 + 2 * 10 / 5 * 5 # term in () first: (3 - 1) => int 2 and (2 + 3) => int 5
  # 2 + 20 / 5 * 5 # * or / next left to right: 2 * 10 => int 20
  # 2 + 4.0 * 5 # * or / next left to right: 20 / 5 => float 4.0
  # 2 + 20.0 # * or / next left to right: 4.0 * 5 => float 20.0
  # 22.0 # + or - next left to right: int 2 is promoted to 2.0, 2.0 + 20.0 => 22.0
  answer = 2 + (3 - 1) * 10 / 5 * (2 + 3)
  print(answer)

def q4():
  # Problem 4
  # My Name: Julia Perrotta
  # values < 7 will not work
  # entering strings will crash the program
  day_start_str = input('What day are you leaving for your trip? (Days 0-6)')
  DAYS = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
  day_start = int(day_start_str)
  trip_length = int(input("Enter length of trip: "))
  day_back = (day_start + trip_length) %7
  print("You will be back on %s" % DAYS[day_back])

def q8():
  # entering a negative value will output garbage
  # entering a string will crash the program
  import math
  radius = int(input("Enter the radius: "))
  math.pi = float(3.14)
  print("The area of a circle with radius %.2f is %.2f" % (radius, math.pi * radius * radius))

def q12():
  # entering string values such as "cat" will crash the program
  # entering values that aren't integers will crash the program
  fahrenheit = int(input("Enter degrees in fahrenheit: "))
  celsius = int((fahrenheit - 32) * (5/9))
  print("%.2f degrees Fahrenheit is %.2f degrees in Celsius" % (fahrenheit, celsius))


q2()
q4()
q8()
q12()
