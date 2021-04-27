# Project 2: Ogopogo - Text Adventure Game

directions = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']
lake_names = ['Vaseux Lake', 'Skaha Lake', 'Lake Okanagan']
lake_o = ['nothing', 'nothing', 'junior Ogopogo', 'nothing', 'canal', 'nothing', 'camera', 'nothing']
lake_s = ['canal', 'camera', 'nothing', 'nothing', 'canal', 'nothing', 'junior Ogopogo', 'camera']
lake_v = ['canal', 'nothing', 'searchlight', 'nothing', 'junior Ogopogo', 'nothing', 'nothing', 'camera']

# Player's position coordinates:
#   the player starts at the south end of Skaha Lake.
current_lake = 1
current_shore = 4

# Items in the player's possession:
#   inventory starts out empty
inventory = []
#   player is allowed a maximum of three items at a time
MAX_ITEMS = 3

# Introduction to game
print("You have rented a canoe in Okanagan Falls,")
print("in hopes of finding and photographing Ogopogo.\n")

# Keep track of whether the game is in progress or over 
#  (so we know when to stop the game loop)
game_state = 'ongoing'

while game_state == 'ongoing':
  # Describe the room the player is in
  if current_lake == 0:
    lake = lake_v
  elif current_lake == 1:
    lake = lake_s
  elif current_lake == 2:
    lake = lake_o
  else:
    game_state = "error1"
    break  # jump out of the game loop if an illegal value is encountered

  print("You are at the " + directions[current_shore] + " shore of " + lake_names[current_lake] + ".")
  current_object = lake[current_shore]
  if current_object == 'canal':
    print('On shore, you can see a canal leading ' + directions[current_shore] + '.')
  # TO DO: handle describing the other cases here.

  # Get command from the player
  choice = input('Command? ')

  # Respond to command
  if choice == 'help':
    # TO DO: display all commands
    # Note that the "pass" keyword in Python is a placeholder for lines where the interpreter would normally expect to see code. If control flow reaches the line with "pass", the interpreter "passes" over the line (i.e. does nothing).
    pass
  elif choice == 'left':
    # TO DO: Player wants to move left
    pass
  elif choice == 'right':
    # TO DO: Player wants to move right
    pass
  elif choice == 'portage':
      current_object = lake[current_shore]
      if current_object != "canal":
          print("Can't portage in this direction -- there is no canal here.")
      else:
        pass # add code here to move to the correct lake
  elif choice == 'grab':
    # TO DO: Player wants to grab item from the shore
    pass
  elif choice == 'shoot':
    # TO DO: Player wants to take a picture of an Ogopogo
    pass
  elif choice == 'inventory':
    # TO DO: Player wants to see what is in current inventory
    pass
  else:
    print('Command not recognized. Type "help" to see all commands.')

if game_state == 'won':
  print('You won the game! :)')
elif game_state == 'error1':
  print('*** A bug was encountered in the program. ***')
  print('Illegal lake index number: ' + str(current_lake))
elif game_state == 'lost':
  print('You lost the game. :( Maybe next time.')
else:
  print('*** A bug was encountered in the program. ***')
  print('Game state variable was set to "' + game_state + '".')

# Starter code
# ------------
# This starter code is intended to help you understand what you're expected to implement.
# It is meant to guide you. Please feel free to make any necessary changes to the code.
# 
# Use the following game specifications as a checklist to ensure
#   that your code has met all of the lab's requirements.
#
# General Overview:
# This game takes place in three connected bodies of water 
#   (Okanagan Lake, Skaha Lake, and Vaseux Lake).
# The player has to traverse the lakes in search of Ogopogo.
#    Along the way they collect items to help with the quest.
# On each move the player has seven possible commands:
#   'left', 'right, 'portage', 'grab', 'shoot', 'inventory', or 'help'.
# If the input is invalid (not one of these commands) the game will let the player know.
# Otherwise, the game will execute the player's command.
# The goal of the game is to successfully take pictures of the elusive Ogopogo.
#
# Game Specifications:
# * The game has three lakes. Each lake is made up of eight shore areas, arranged
#   in a cycle: north, northeast, east, southeast, south, southwest, west, northwest.
# * A shore can contain: a canal (to a neighboring lake), a camera,
#   a searchlight, a juvenile Ogopogo, a parent Ogopogo, or nothing.
# * At the start of the game, the player is in a small canoe
#   on the south end of Skaha Lake.
# * The player can move to an adjacent shore by typing the 'left' command
#   to move counterclockwise along the shore, or 'right' to move clockwise.
# * The player can also move from one lake to another by typing 'portage',
#   if and only if the current shore contains a canal.
# * The game prints out the contents of the current shore after every command.
# * The player can grab a camera or searchlight if they pass a shore.
#   The camera or searchlight is no longer on that shore once grabbed.
# * Juvenile Ogopogos are blocking the passage of canoes near some shores.
#   The player can use a flash camera to startle an Ogopogo into flight
#   (they're notoriously camera-shy) using the 'shoot' command.
#   Startled Ogopogos swim away to alert their parent of the player's presence.
# * Flash cameras are single-shot, and are removed from the player's inventory
#   after use. The story line might explain that the cameras are lost overboard
#   in the encounter, ruined by water from a splash, etc. Camera flashes are not
#   strong enough to allow for a successful picture.
# * If they have no camera, the player can paddle back in the direction
#   from which they came. If the player attempts to continue in the same
#   direction past a juvenile or parent Ogopogo, their canoe will be capsized
#   and sunk, and the game will end.
# * Once three juveniles have been startled, the parent surfaces in
#   Lake Okanagan to defend the family.
# * To take a successful picture of the parent Ogopogo and complete the game,
#   a searchlight is needed in inventory as well as a camera.
# * The 'inventory' command shows the items currently in the player's inventory.
# * The game should be implemented using lists.
# * Use a list to keep track of the player's items. At the beginning of the game
#   the player's inventory list should be empty.
# * A maximum of three items can be held in the inventory at once.
# * The player can only portage to the next lake if the current shore contains a canal.
# * Canals are only present in the north and south shores,
#   since this is a north/south oriented chain of lakes.
# * A canal will move the player to the next lake in the chain in that direction.
#   For example, a canal in the north shore moves the player to the next lake to the north.
# * Continuing clockwise (right) around any lake from the northwest shore (index 7)
#   will bring the player back to the north shore (index 0).
# * Continuing counter-clockwise (left) around any lake from the north shore (index 0)
#   will bring the player back to the northwest shore (index 7).

'''
NOTE: All text inside triple quote marks, as shown here,
  will be ignored by Python, even if it extends onto multiple lines.
    
Checkpoints
-----------
To complete the lab successfully, divide up the coding task into a series of checkpoints.
At each checkpoint, test all of the game features that have been implemented so far,
to make sure that new code hasn't caused any bugs in features from previous checkpoints.

Sample checkpoints
------------------
These can be checked off here as coding progresses. This can help keep the class in sync,
  make it easier to find trouble spots, and give opportunities to cover common problems.

Checkpoint 0: Report current room contents correctly.  
  Implement "help" command.
  Complete? Student:     Teacher/Volunteer: 

Checkpoint 1: Implement "left" and "right".
  Test and correct for moves to positions -1 and 8 (completing a circle around a lake).
  Optional: write code that will still work if shore list length is changed.
  Complete? Student:     Teacher/Volunteer:

Checkpoint 2: Implement "portage", only at positions where a canal is present.
  Movement direction is different if player position is north vs. south shore.
  Complete? Student:     Teacher/Volunteer:

Checkpoint 3: Record the player's last movement direction.
  If an Ogopogo is present on a given shore, allow players to exit only in the direction
  from which they entered. Otherwise, print an appropriate "game over" message.
  Complete? Student:     Teacher/Volunteer:

Checkpoint 4: Implement "grab" command
  Start by allowing unlimited inventory. Test for bugs. Then
  * Check inventory list length before starting "grab".
    Print a refusal message if inventory list is already length 3.
    The item the player tried to grab should not be affected.
  * Ogopogos and canals can never successfully be added to inventory.
  Complete? Student:     Teacher/Volunteer:

Checkpoint 5: Implement "inventory" command
  Decide how to list inventory in a user-friendly way
    -- not just "print(inventory)", though that makes a good start.
  Do not allow visible brackets or quotation marks in text printed for the player.
  Optional: write code that will still work if MAX_ITEMS global variable is changed.

Checkpoint 6: Implement "shoot" command.  
  Check inventory for appropriate item(s) needed to photograph each type of Ogopogo.
  For junior Ogopogos, remove camera after each photography attempt,
    with appropriate print() statements telling the story of how this happens.
  Complete? Student:     Teacher/Volunteer:

Checkpoint 7:  Acknowledge a win if photography attempt is successful.
  Go through each of the specs again and confirm that the code works correctly.
  Complete? Student:     Teacher/Volunteer:
'''