# Alternate Project 7: Mailing List

In this project, you will create a program that creates mailing lists so that advertisers can send bulk emails to people based on their
specific interests.

## Overview


### Implementation Details

* Use classes to build off the implemented base class for Pokemon. Keep track of HP, Max AP, and type.
  * Here is some [starter_code]
* Design classes for Fire, Grass, Water Types that inherit from the base Pokemon Class
* Each Pokemon should be an instance, use a master list to store all the Pokemon and create this the beginning of the game
* Use methods to set the Pokemon for each player and remove those pokemon from the master Pokemon list.
* Player's and Computer's Pokemon should be stored using a list
* Pokemon attacks should be stored using a dictionary from the attack name to a list of [attack's power, attack's accuracy]

## Solution

```python
class Person:

  def __init__(self, name, email, hobbies):
    self.name = name
    self.email = email
    self.hobbies = hobbies

  def __str__(self):
    return f'{self.email} {self.name} {self.hobbies}'


class Mailer:

  def __init__(self):
    self.people = []

  def __str__(self):
    return '\n'.join(str(p) for p in self.people)
  
  def send_hobby_mailer(self, hobby):
    to_send = []
    for person in self.people:
      if hobby in person.hobbies:
        to_send.append(person.email)
    print('Mailing ' + hobby + ' to: ' + str(to_send))
    return to_send
  
  def count_hobbies(self):
    results = {}
    for person in self.people:
      for hobby in person.hobbies:
        if hobby in results.keys():
          results[hobby] += 1
        else:
          results[hobby] = 1
    print('Hobby Results')
    print(results)
  
  def already_present(self, check):
    for person in self.people:
      if person.email == check.email:
        print(person.email + ' is already in our list')
        return person
    print(check.email + ' is not in our list')
    return None

  def add_person(self, check):
    result = self.already_present(check)
    if result is None:
      print(check.email + ' has been added to our list')
      self.people.append(check)
    else:
      for hobby in check.hobbies:
        if hobby not in result.hobbies:
          print('Added ' + hobby + ' to ' + check.email + '\' hobbies')
          result.hobbies.append(hobby)


mailer = Mailer()
while True:
  command = input('What would you like to do? (add, count, send, display, exit) ')
  if command == 'add':
    who = input('Enter name email and hobbies: ').split(' ')
    mailer.add_person(Person(who[0], who[1], who[2].split(',')))
  elif command == 'count':
    mailer.count_hobbies()
  elif command == 'send':
    hobby = input('Which hobby? ')
    mailer.send_hobby_mailer(hobby)
  elif command == 'display':
    print(mailer)
  elif command == 'exit':
    print('Goodbye')
    break
  else:
    print('Sorry, I did not understand that')


mailer = Mailer()
mailer.add_person(Person('Alice', 'a_dog@host.com', ['dogs', 'animals']))
mailer.add_person(Person('Bob', 'knitting@host.com', ['knitting', 'surfing', 'painting']))
mailer.add_person(Person('Carlos', 'filmbuff@host.com', ['movies']))
mailer.add_person(Person('Daisy', 'soccerfan@host.com', ['soccer', 'tennis', 'dogs']))
mailer.add_person(Person('Eva', 'everything@host.com', ['surfing', 'movies', 'knitting', 'animals']))

print(mailer)

# all people should be added without problem and printed

#below person should be added without issue. The name is the same but email is different
mailer.add_person(Person('Bob', 'another_bob@host.com', ['cats', 'tennis']))

# this Bob already exists in the mailer (same email address). Add Bob's NEW hobbies to the list
mailer.add_person(Person('Bob', 'knitting@host.com', ['surfing', 'animals', 'poetry']))

print(mailer)

mailer.count_hobbies()

mailer.send_hobby_mailer('animals')
mailer.send_hobby_mailer('tennis')
mailer.send_hobby_mailer('unique')

```

## Grading

TO BE UPDATED

### Scheme/Rubric

| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| Players can choose pokemon hand | 15   |
| Computer randomly picks hand | 5|
| Player can choose pokemon to battle  | 5   |
| Stats, Move, and  All stats print properly           | 10  |
| Attack command decreases HP properly      | 10 |
| **Sub total**                                                   | 45  |
| **Technical Correctness**                                    |     |
| Correct use of classes                                  | 10  |
| Correct use of inheritance                                  | 10  |
| Correct use of instances                                  | 10  |
| Correct use of variables and game loop |10|
| Correct use of printing/formatting | 10|  
| **Sub total**                                                   | 50  |
| **Total**                                                       | 95 |

[starter_code]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/units/7_unit/05_lesson/starter_code.py
