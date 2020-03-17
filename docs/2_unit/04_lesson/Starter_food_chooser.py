food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('answers will be taken as y or n')
user_input = input('Do you like food with holes ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

