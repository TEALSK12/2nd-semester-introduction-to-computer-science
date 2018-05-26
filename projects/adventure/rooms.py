
rooms = {
    "entryway":
        { "description": "You awaken to find yourself in a dark room.\nYou feel a little woozy...\n\nDo you lie back down and rest again?",
          "directions": {"yes": "gremlin", "no": "hall"} },
    "gremlin":
        { "description": "You lie back down and soon drift off to sleep...\n\nStartled you awaken again noticing a pair of beady eyes staring back at you and a tongue poised on your ankle.\n\nDo you KICK the creature or slowly PULL your leg away?",
          "directions": {"kick": "end", "pull": "end"} },
    "hall":
        { "description": "You decide to explore your environment a bit more...\n\nStumbling through the dark, you soon come across a heavy wooden door.\n\nIt creaks and groans loudly as you swing it open.\n\nBefore you lays a dimly lit corridor proceeding both LEFT and RIGHT.",
          "directions": {"left": "end", "right": "end"} },
    }

currentroom = "entryway"

while input != "exit":
    print rooms[currentroom]["description"]

    input = raw_input(">").lower()

    if input != "exit":
        if input in rooms[currentroom]["directions"]:
            currentroom = rooms[currentroom]["directions"][input]
        else:
            print "That's not a choice here, try one of the following: " + repr(rooms[currentroom]["directions"].keys())
