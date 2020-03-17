
text = "not exit"
while text != "exit":

    print "You are on a deserted island.  There is a palm tree in front of you and a coconut on the ground."

    text = raw_input("now what??? ")

    if text == "go north":
        print "This is an island, you can't go that way."
    elif text == "pick up coconut":
        print "You pick up the coconut and put it in your pocket."
    else:
        print "You can't do ' " + text + " ' here."
