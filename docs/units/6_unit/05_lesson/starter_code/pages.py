# Functions related to the display of a paginated list with a 
# fixed number of items per page. This code is part of the TEALS
# Unit 6 project, "Buy an Umbrella".

# Returns the index of the first item on the named page of
# a paginated list with a fixed number of items per page.
# The lowest valid page number is 0 (not 1).
# Returns None if there are not enough items to reach the 
# page number requested.
def first_index(num_items, page_number, items_per_page):
  if page_number * items_per_page < num_items:
    return page_number * items_per_page
  else:
    return None


# Returns the index of the last item on the named page of
# a paginated list with a fixed number of items per page.
# Returns None if there are not enough items to reach the 
# page number requested.
def last_index(num_items, page_number, items_per_page):
  if page_number * items_per_page < num_items:
    return min(num_items, (page_number + 1) * items_per_page) - 1
  else:
    return None
  
  
# Returns the next page number for a paginated display of a list.
# This is usually one more than the current page number, but if you've
# reached the end of the list, there is no "next page", in which case
# we just return the current page number.
def next_page_number(num_items, current_page_number, items_per_page):
  if (current_page_number + 1) * items_per_page < num_items:
    return current_page_number + 1
  else:
    return current_page_number
  
  
# Returns the previous page number for a paginated display of a list.
# This is usually one less then the current page number, but if you've
# reached the beginning of the list, there is no "previous page", in which
# case we just return the current page number (which is necessarily 0)
def previous_page_number(current_page_number):
  if current_page_number > 0:
    return current_page_number - 1
  else:
    return 0
