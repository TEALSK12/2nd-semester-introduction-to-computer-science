# Sample starter code for Cross Country Canada

# List assumptions of your Cross Country Canada game
# Some examples:
#   Travel is always West. Starts in Vancouver and ends in Halifax.
#	The player eats 5 kg of food every day
# 	The player travels between 500km to 1200km each trip, and takes 1-3 days
#	... etc. 

# welcome the user and explain the game rules
welcome_text = """
Welcome to the Cross Country Canada! 

"""

# explain the actions user can take
help_text = """
Each turn you can take one of following actions:

  travel - 
  rest	- 
  buy food  - 
  get commodity - 


When prompted for an action, you can also enter one of these commands without using up your turn:

  status - lists location, health, distance traveled, food available, commodities collected and day of travel.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'b', 'g', 's', '?', 'q'
  
"""

# Variables -- variable that collectively represent the state of the game
## What else will you need to keep track in this game?
player_name = ""
days_traveled = 0
distance_traveled = 0


# Constants -- parameters that define the rules of the game, which don't change.
## What other constants will you need to define?
MIN_KM_PER_TRAVEL = 500
MAX_KM_PER_TRAVEL = 1200
MIN_DAYS_PER_TRAVEL = 1
MAX_DAYS_PER_TRAVEL = 3

## add more cities
CITIES = [
    'Vancouver, BC', 'Halifax, NS'
]

# add commodities


# functions
# assign player a list of commodities
def print_dispatch_notice():
	# randomly select commodities to deliver for this trip

	# creat dispatch notice text and print
	dispatch_notice_text = ""
	print(dispatch_notice_text)
	
	
# handle the buy food command
def handle_buy_food():
	# purchase a random amount of food as defined by the game rules

	buy_food_text = ""
	print(buy_food_text)

# handle the travel command
def handle_travel():

	# moves player randomly between MIN_KM_PER_TRAVEL and MAX_KM_PER_TRAVEL

	travel_text = ""
	print(travel_text)

# handle the rest command
def handle_rest():
	rest_text = ""
	print(rest_text)

# handle the get command
def handle_get_commodity():

	# check if the player has arrived at a city

	# print result
	get_commodity_text = ""
	print(get_commodity_text)

# handle the status command
def handle_status():
	print("Here's the status:")

	# create the report on current status

# handle the help command
def handle_help():
	print(help_text)

# handle the quit command
def handle_quit():
	global playing
	playing = False

# handle invalid user action
def handle_invalid_input(response):
	print("'{0}' is not a valid command. Try again.".format(response))

# check if the game is over, returns a boolean
def game_is_over():
	return False #update the function to check if the game is over 

# check if the player won, return a boolean
def player_wins():
	return True #update the function to check if the player won



print(welcome_text + help_text)
player_name = input("\nWhat is your name? ")


playing = True # if playing = True, continue the game
print_dispatch_notice()

handle_status()
while playing:
	print()
	action = input("Choose an action, {0}: ".format(player_name))
	if action == "travel" or action == "t":
		handle_travel()
	elif action == "rest" or action == "r":
		handle_rest()
	elif action == "buy food" or action == "b":
		handle_buy_food()
	elif action == "get commodity" or action == "g":
		handle_get_commodity()	
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
	print("\n\nCongratulations, you made it!")
	handle_status()
else:
	print("\n\nYou did not complete the mission.")
	handle_status()