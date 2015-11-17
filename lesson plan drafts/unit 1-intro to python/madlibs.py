print("Day in New York City: A Mad Lib")
print("Instructions. The program will prompt for a type of word to enter. After all words are entered the program will print a story")

user_name = input("Enter a proper noun: ")
location = input("Enter a place: ")
destination = input("Enter another place: ")
adverb = input("Enter an adverb: ")
distraction = input("Enter a noun: ")
distraction_description = input("Enter an adjective: ")
action_description = input("Enter an adverb: ")
action = input("Enter a verb: ")
new_location = input("Enter a place")
final_description = input("Enter an adjective: ")

introduction =  "It was a beautiful day in New York City. Our hero " + user_name + " was on a walk from " + location + " to " + destination + "."
background = user_name + " was walking rather " + adverb + " because he/she had lived in New York for a few months."
distraction_part = "All of a suden a " + distraction_description + " " + distraction + " appeared out of nowhere!!!"
get_away = user_name + " decided to " + action + " " + action_description + " instead of dealing with the situation."
finale = "Thrown off from " + destination + " " + user_name + " decides to go to " + new_location + "instead."
summation = "What a " + final_description + " day in New York."

print(introduction + background + distraction + get_away + finale + summation)



