food = ['donuts', 'pancakes', 'bacon', 'waffles', 'eggs', 'bagels']
score = [0,0,0,0,0,0]

print('Please answer each question with "y" for "yes" and "n" for "no".')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

# Add remaining questions here, and adjust scores similar to the above.