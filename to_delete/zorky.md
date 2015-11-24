```
maze = [["stairs down", "monster", "nothing", "sword", "nothing", "monster"],
["nothing", "stairs up", "nothing", "magic crystals", "stairs down", "sword" ],
["PRIZE", "boss monster", "nothing", "nothing", "stairs up", "monster"]]
is_alive = True
user_horizontal = 4
user_vertical = 0
user_pocket = []
won = False
while is_alive and not won:
    user_input = input("What would you like to do? ")
    previous_obstacle = maze[user_vertical][user_horizontal]
    if previous_obstacle == "monster" or previous_obstacle == "boss monster":
        if user_input == "right" or user_input == "left" or user_input == "up" or user_input == "down":
            print("Monster has fatally wounded you :(")
            is_alive = False
            break
    if user_input == "right":
        user_horizontal+=1
        if user_vertical < 0 or user_vertical >= len(maze) or user_horizontal < 0 or user_horizontal >= len(maze[user_vertical]):
            print("Sorry can't go that way.")
        else:
            print("You see " + maze[user_vertical][user_horizontal])
    elif user_input == "left":
        user_horizontal-=1
        if user_vertical < 0 or user_vertical >= len(maze) or user_horizontal < 0 or user_horizontal >= len(maze[user_vertical]):
            print("Sorry can't go that way.")
        else:
            print("You see " + maze[user_vertical][user_horizontal])
    elif user_input == "up":
        if previous_obstacle != "stairs up":
            print("Cannot go that way.")
        else:
            user_vertical-=1
        if user_vertical < 0 or user_vertical >= len(maze) or user_horizontal < 0 or user_horizontal >= len(maze[user_vertical]):
            print("Sorry can't go that way.")
        else:
            print("You see " + maze[user_vertical][user_horizontal])
    elif user_input == "down":
        if previous_obstacle != "stairs down":
            print("Cannot go that way.")
        else:
            user_vertical +=1
        if user_vertical < 0 or user_vertical >= len(maze) or user_horizontal < 0 or user_horizontal >= len(maze[user_vertical]):
            print("Sorry can't go that way.")
        else:
            print("You see " + maze[user_vertical][user_horizontal])
    elif user_input == "fight":
        obstacle = maze[user_vertical][user_horizontal]
        if obstacle == "boss monster":
            if "sword" in user_pocket and "magic crystals" in user_pocket:
                print("You defeated the boss monster and won!")
                user_pocket.remove("sword")
                user_pocket.remove("magic crystals")
                maze[user_vertical][user_horizontal] = "nothing"
                won = True
            elif "magic crystals" in user_pocket:
                print("You wounded the boss monster!")
                user_pocket.remove("magic crystals")
                maze[user_vertical][user_horizontal] = "monster"
        elif obstacle == "monster" and  "sword" in user_pocket:
            print("You defeated the monster!")
            user_pocket.remove("sword")
            maze[user_vertical][user_horizontal] = "nothing"
        elif obstacle == "monster":
            print ("You have been defeated :( ")
            is_alive = False
        else:
            print("You can't fight that!")
    elif user_input == "grab":
        obstacle = maze[user_vertical][user_horizontal]
        if obstacle == "sword" or obstacle == "magic crystals":
            print("Picked up " + obstacle)
            maze[user_vertical][user_horizontal] = "nothing"
            user_pocket.append(obstacle)
        else:
            print("You can't pick up that!")
    elif user_input == "commands":
        print("Commands are: right, left, up, down, fight, run, grab, and commands")
    else:
        print("Sorry that input wasn't recognized. Type commands to get all possible commands")


```