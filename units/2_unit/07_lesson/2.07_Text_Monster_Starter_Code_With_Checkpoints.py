# Lab 2.07: Text Monster - Starter Code
# The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level.
floor0 = ['empty', 'a sword', 'stairs up', 'a monster', 'empty']
floor1 = ['magic stones', 'a monster', 'stairs down', 'empty', 'stairs up']
floor2 = ['a prize', 'a boss monster', 'a sword', 'a sword', 'stairs down']

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'

while gameState == 'ongoing':
  # Describe the room the player is in
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2

  room = floor[currentRoom]
  
  if room == 'empty':
    print('You are in an empty room.')
  # TO DO: Handle describing the other cases here

  # Get command from the player
  choice = input('Command? ')

  # Respond to command
  if choice == 'help' or choice == 'h':
    # Help: display all commands
    # The "pass" keyword is a placeholder for lines where the Python interpreter
    #   would normally expect to see code. If control flow reaches a "pass" line,
    #   the interpreter "passes" over the line (i.e. does nothing).
    #   Gradually replace all these 'pass' statements with code that implements each command.
    pass
  elif choice == 'left' or choice == 'l':
    # Player wants to move left
    pass
  elif choice == 'right' or choice == 'r':
    # Player wants to move right
    pass
  elif choice == 'up' or choice == 'u':
    # Player wants to go upstairs
    pass
  elif choice == 'down' or choice == 'd':
    # Player wants to go downstairs
    pass
  elif choice == 'grab' or choice == 'g':
    # Player wants to grab item from the room
    pass
  elif choice == 'fight' or choice == 'f':
    # Player wants to fight monster in the room
    pass
  else:
    print('Command not recognized. Type "help" to see all commands.')

if gameState == 'won':
  print('You won the game! :)')
else:
  print('You lost the game. :( Maybe next time.')

'''
  NOTE: All text inside triple quote marks, as shown here,
    will be ignored by Python, even if it extends onto multiple lines.
  
  Starter code
  ------------
  This starter code is intended to help you understand what you're expected to implement.
  It is meant to guide you. Please feel free to make any necessary changes to the code. 
  
  Use the following game specifications as a checklist to ensure
  that your code meets all of the requirements of the lab.
  
  Game specifications
  -------------------
  This game takes place in a three-floor virtual space/dungeon.
  Each floor has five rooms, arranged in a line from left to right.
  The whole map must contain at least 3 floors and 15 rooms total.
  
  The game's code should be designed so that the dungeon map can be changed
    just by redefining the initial lists, without changing any other code.

  On each move the player has seven possible commands: 'left', 'right', 'up', 'down', 'grab', 'fight' or 'help'. 
  The player can try to move to the left room or right room.
  If there is no room in that direction, the game should report this.
  The player cannot move outside the boundaries of the virtual world.
  The player can also move upstairs or downstairs if the room contains an up-staircase or a down-staircase.
  
  The game prints out the contents of the current room after every command.
    This can be implemented by printing "In this room you see [item]." after the player chooses a command.
  The player can grab swords or magic stones if they walk into a room with them.
  The sword or stones are no longer in the room once grabbed.
  Your virtual world should have a minimum of 4 swords.
  Your virtual world must have a minimum of 1 magic stone.
  
  The player can use a sword to defeat a monster using the 'fight' command.
  The sword and monster disappear after fighting.
  If they have no sword, the player can exit in the direction from which they came.
  If the player fights without a sword, they will be defeated and the game will end.
  If they try to walk past a monster, they will be defeated and the game will end.
  There should be three regular monsters placed throughout the game. These require a sword to defeat.
  There should be a boss monster in the room just before the room that contains the prize.
  The boss monster requires magic stones and a sword to defeat.
  
  The game is won when the player grabs the prize after defeating the boss monster
  The game is lost if the player:
  1. Fights a monster without a sword
  2. Fights the boss monster without a sword and stones
  3. Tries to move past the monster
  
  Use a list to keep track of the player's items.
  At the beginning of the game, it should be empty.
  Players can hold a maximum of three items.
  
  Checkpoints
  -----------
  To complete the lab successfully, divide up the coding task into a series of checkpoints.
  At each checkpoint, test all of the game features that have been implemented so far,
  to make sure that new code hasn't caused any bugs in features from previous checkpoints.
  
  Sample checkpoints
  ------------------
  (These can be checked off here as coding progresses. This can help keep the class in sync,
    make it easier to find trouble spots, and give opportunities to cover common problems.)
  
  Checkpoint 0:
    Report current room contents correctly.
    Implement "help" command.   
    Complete? Student:     Teacher/Volunteer: 
  
  Checkpoint 1: 
    Make "up", "down", "left", and "right" work correctly.
    Do not need error checking.
    Complete? Student:     Teacher/Volunteer:
  
  Checkpoint 2: 
    Add all error checks and messages related to movement.
    It should not be possible to:
     * move off the map
     * go up and down unless the right staircase is present
    Complete? Student:     Teacher/Volunteer:
  
  Checkpoint 3:
    Record the player's last movement direction.
    If a room contains a monster, allow players to exit only in the direction from which they entered.  
    Otherwise, print an appropriate "game over" message.
    Complete? Student:     Teacher/Volunteer:
  
  Checkpoint 4: Implement "grab" command
    Start by allowing unlimited inventory. Test for bugs. Then
    * Check inventory list length before starting "grab".
    * Print a refusal message if list is already length 3.
      The item the player tried to grab should not be affected.
    * Monsters and stairs can never successfully be added to inventory.
    Complete? Student:     Teacher/Volunteer:
  
  Checkpoint 5:
    Implement "fight" command.  
    Check inventory for appropriate item(s) to defeat each monster / boss monster.
    Remove those items after successful fight.
    Complete? Student:     Teacher/Volunteer:
  
  Checkpoint 6:
    Decide what happens when the prize is picked up.
    Go through each of the specs again and confirm that the code works correctly.
    Complete? Student:     Teacher/Volunteer:
'''