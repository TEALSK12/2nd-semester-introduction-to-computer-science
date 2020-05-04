# TEALS Unit 6 Project -- Buy an umbrella

from criteria import criteria_to_string
from criteria import filter_items
from dictionaries import union_of_dictionaries
from items import item_to_string
from items import load_items
from items import print_page
from pages import first_index
from pages import last_index
from pages import next_page_number
from pages import previous_page_number
from TEALS_utils import get_valid_integer

welcome_text = '''Welcome to Umbrellas Unlimited, your online market for water
protection. We have over 100 umbrellas for sale. Happy shopping!
'''

help_text = '''Use these commands to navigate our site:
  (n)ext          - view the next page of items
  (p)revious      - view the previous page of items
  (a)dd filter    - narrow your search by adding criteria
  (r)emove filter - broaden your search by deleting criteria
  (m)odify filter - change your search criteria
  (b)uy           - purchase an umbrella from the list shown
  (q)uit          - exit our site
'''

action_prompt = '(b)uy, (n)ext, (p)revious, (a)dd, (r)emove, '
action_prompt += '(m)odify, (h)elp or (q)uit?'


# Prompts the user for an item to buy, then prints out a short description
# of the purchased item. A list of items is provided as input, as well as
# the start and end indices of a range of items that may be
# purchased. items[min_item] and items[max_item] may each be purchased.
#
# Returns nothing.
def handle_purchase(items, page_number, items_per_page):
  print('TODO(student): handle_purchase() not implemented yet!')
    
    
# Prompts the user for an item attribute and a value to allow for that
# attribute, then adds a new criterion to the input criteria dictionary.
# Because dictioaries in Python are passed by reference, the input criteria
# are mutated as a result of this function call.
#
# Returns nothing.
def handle_add_criterion(criteria):
  print('TODO(student): handle_add_criterion() not implemented yet!')


# Shows the user the existing criteria that have been specificed and
# prompts the user to select one to remove entirely. To remove just one
# value from a criterion but leave others, use handle_modify_criterion()
# rather than handle_remove_criterion().  Because dictioaries in Python are
# passed by reference, the input criteria are mutated as a result of this
# function call.
#
# Returns nothing
def handle_remove_criterion(criteria):
  print('TODO(student): handle_remove_criterion() not implemented yet!')


# Shows the user the existing criteria that have been specificed and
# prompts the user to select one to modify. Then prompts the user to select
# a possible value for that attribute. The chosen value is flipped, either
# from allowed to excluded, or from excluded to allowed, depending on its
# current status. Because dictioaries in Python are passed by reference,
# the input criteria are mutated as a result of this function call.
#
# Returns nothing.
def handle_modify_criterion(criteria):
  print('TODO(student): handle_modify_criterion() not implemented yet!')

  
## Main program      
umbrellas = load_items('inventory.txt')
umbrella_possibilities = union_of_dictionaries(umbrellas)
umbrella_attributes = list(umbrella_possibilities.keys())
items_per_page = 5
page_number = 0
current_criteria = {} 

print(welcome_text)
print(help_text)

running = True
while running:
  if current_criteria:
    print('Current filters: \n' +
      criteria_to_string(current_criteria))
  filtered_items = filter_items(current_criteria, umbrellas)
  num_items = len(filtered_items)
  print_page(filtered_items, page_number, items_per_page)

  action = input('\n' + action_prompt)
  if action == 'next' or action == 'n':
    page_number = next_page_number(num_items, page_number, items_per_page)
  elif action == 'previous' or action == 'p':
    page_number = previous_page_number(page_number)
  elif action == 'add' or action == 'a':
    handle_add_criterion(current_criteria)
    page_number = 0
  elif action == 'remove' or action == 'r':
    handle_remove_criterion(current_criteria)
    page_number = 0
  elif action == 'modify' or action == 'm':
    handle_modify_criterion(current_criteria)
    page_number = 0
  elif action == 'buy' or action == 'b':
    handle_purchase(filtered_items, page_number, items_per_page)
    running = False
  elif action == 'help' or action == 'h':
    print(help_text)
  elif action == 'quit' or action == 'q':
    running = False
  else:
    print("Sorry, I don't know that that means.")
