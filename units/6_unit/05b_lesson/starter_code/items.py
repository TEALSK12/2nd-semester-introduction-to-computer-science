# Functions related to representing shopping items as a python
# dictionary. This code is part of the TEALS Unit 6 project, 
# "Buy an Umbrella".

from pages import last_index
from pages import first_index

# Loads a file containing a list of available shopping items, returns
# the contents as a list of dictionaries.
#
# The file is in "comma separated value" (or CSV) format. Each item is
# described by a number of attributes, like its brand, size, price,
# etc. The first line (the "header line") of the file names what each
# of these attributes is. The rest of the file is one line per item,
# each line containing the values of those attributes for the
# particular item it represents. The order of the values is consistent
# with the order of the attributes in the header line. For example
# 
#      color,weight,price
#      red,4 lbs.,$8.50
#      green,2 lbs.,$7.00
# 
# represents two items, a four-pound red item that costs $8.50 and a
# two-pound green item that costs $7.
#
# load_items() transforms each non-header line into a dictionary. The
# keys are the attributes named in the header line. The values are the
# contents of the non-header line. It returns a list of these
# dictionaries, one per non-header line of the file.
def load_items(filename):
  print('TODO(student): load_items() not implemented yet.')
  # This code will get you started. They read the named file into
  # memory as one very large string, then split it into the indivdual
  # lines as found in the file. You need to write code that does something
  # with each line.
  file = open(filename, "r")
  bulk_data = file.read()
  file.close()
  lines = '\n'.split(bulk_data)
  # TODO(student): do something with the header line, and do something with 
  # each of the non-header lines.
  return []


# Given a dictionary representation of an item, returns a short
# description of the item. This version is tailored to write good
# descriptions of umbrellas, but you could imagine slight variants for
# other products.
def item_to_string(item):
  print('TODO(student): item_to_string() not implemented yet.')
  return 'item string'
  
    
# Prints the items that occupy a given page of
# a paginated list with a fixed number of items per page.
def print_page(items, page_number, items_per_page):
  num_items = len(items)
  first = first_index(num_items, page_number, items_per_page)
  last = last_index(num_items, page_number, items_per_page)
  if first is not None and last is not None:
    print('\nShowing items {0}-{1} of {2} items\n'.format(
    first + 1, last + 1, num_items))
    for i in range(first, last + 1):
      print('{0:3d}) {1}'.format(i + 1, item_to_string(items[i])))
  else:
    print('\nNo matching items. Try relaxing some of your filters')