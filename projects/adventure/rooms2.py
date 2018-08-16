
descriptions = {
    "entryway": "You awaken to find yourself in a dark room.\nYou feel a little woozy...\n\nDo you lie back down and rest again?",
          
    "gremlin": "You lie back down and soon drift off to sleep...\n\nStartled you awaken again noticing a pair of beady eyes staring back at you and a tongue poised on your ankle.\n\nDo you KICK the creature or slowly PULL your leg away?",
          
    "hall": "You decide to explore your environment a bit more...\n\nStumbling through the dark, you soon come across a heavy wooden door.\n\nIt creaks and groans loudly as you swing it open.\n\nBefore you lays a dimly lit corridor proceeding both LEFT and RIGHT.",

    "end": "Your adventure has ended."
    }

directions = {
    "entryway": {"yes": "gremlin", "no": "hall"},
    "gremlin": {"kick": "end", "pull": "end"},
    "hall": {"left": "end", "right": "end"},
    }

currentroom = "entryway"

text = "not exit"
while text != "exit":
    print descriptions[currentroom]

    text = raw_input(">").lower().strip()

    if text != "exit":
        if text in directions[currentroom]:
            currentroom = directions[currentroom][text]
        else:
            print "That's not a choice here, try one of the following: " + repr(directions[currentroom].keys())
