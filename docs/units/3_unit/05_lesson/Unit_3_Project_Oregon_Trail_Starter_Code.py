# Simulation game of traveling out west in 1800's

import random

welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are
headed out West to populate the frontier. Your goal is to travel
by wagon train from Independence, MO to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck, and see you in Oregon!"

# Model -- variables that collectivel represent the state
# of the game
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_suffered_this_month = 0
player_name = None

# Constants -- parameters that define the rules of the game,
# but which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5

FOOD_PER_HUNT = 100
MIN_DAYS_PER_HUNT = 2
MAX_DAYS_PER_HUNT = 5

FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'fake', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]


# Converts are numeric date into a string.
# input: m - a month in the range 1-12
# input: d - a day in the range 1-31
# output: a string like "December 24".
# Note: this function does not enforce calendar rules. It's happy to output
# impossible strings like "June 95" or "February 31"
def date_as_string(m, d):
	# Enter your code here


def date_report():
	# Enter your code here


def miles_remaining():
	# Enter your code here


# Returns the number of days in the month (28, 30, or 31).
# input: an integer from 1 to 12. 1=January, 2=February, etc.
# output: the number of days in the month. If the input is not in
#   the required range, returns 0.
def days_in_month(m):
	# Enter your code here
 
# Calculates whether a sickess occurs on the current day based
# on how many days remain in the month and how many sick days have
# already occured this month. If there are N days left in the month, then
# the chance of a sick day is either 0, 1 out of N, or 2 out of N, depending
# on whether there have been 2 sick days so far, 1 sick day so far, or no
# sick days so far.
#
# This system guarantees that there will be exactly
# 2 sick days each month, and incidentally that every day of the month
# is equally likely to be a sick day (proof left to the reader!)
def random_sickness_occurs():
	# Enter your code here

def handle_sickness():
	# Enter your code here

def consume_food():
	# Enter your code here

# Repairs problematic values in the global (month, day) model where the day is
# larger than the number of days in the month. If this happens, advances to the next
# month and knocks the day value down accordingly. Knows that different months have
# different numbers of days. Doesn't handle cases where the day is more than 28
# days in excess of the limit for that month -- could still end up with an
# impossible date after this function is called.
#
# Returns True if the global month/day values were altered, else False.
def maybe_rollover_month():
	# Enter your code here

# Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness. The sickness rules are quirky: player
# is guaranteed to fall ill a certain number of times each month, so illness
# needs to keep track of month changes.
#
# input: num_days - an integer number of days that elapse.
def advance_game_clock(num_days):
	# Enter your code here

def handle_travel():
	# Enter your code here

def handle_rest():
# Enter your code here

def handle_hunt():
	# Enter your code here

def handle_status():
	# Enter your code here

def handle_help():
# Enter your code here

def handle_quit():
	global playing
	playing = False


def handle_invalid_input(response):
	print("'{0}' is not a valid command. Try again.".format(response))


def game_is_over():
	# Enter your code here

def player_wins():
	# Enter your code here

def loss_report():
	# Enter your code here

print(welcome_text + help_text + good_luck_text)
player_name = input("\nWhat is your name, player?")

playing = True
handle_status()
while playing:
	print()
	action = input("Choose an action, {0} -->".format(player_name))
	if action == "travel" or action == "t":
		handle_travel()
	elif action == "rest" or action == "r":
		handle_rest()
	elif action == "hunt" or action == "h":
		handle_hunt()
	elif action == "quit" or action == "q":
		handle_quit()
	elif action == "help" or action == "?":
		handle_help()
	elif action == "status" or action == "s":
		handle_status()
	else:
		handle_invalid_input(action)

	if game_is_over():
		playing = False

if player_wins():
	print("\n\nCongratulations you made it to Oregon alive!")
	handle_status()
else:
	print("\n\nAlas! You lose.")
	handle_status()
	print(loss_report())
