# Tries to interpret a string as an integer, returns the
# result. returns a default value if the interpretation fails.
def safe_to_integer(value, default=0):
  try:
    return int(value)
  except (ValueError, TypeError):
    return default

# Prompts user for an integer input that must be in some range.  Keeps
# asking for a valid value until the user provides one in that range.
# min_value and max_value are both valid responses.  Returns:
# user-supplied integer. Guaranteed to be within range.
def get_valid_integer(prompt, min_value, max_value):
	valid = False
	while not valid:
		value = safe_to_integer(input(prompt + "--> "))
		if value < min_value or value > max_value:
			print("Enter a value from {0} to {1}. Try again.".format(
			    min_value, max_value))
		else:
			valid = True
	return value
