import re

# Your input string
s = "Granola Bar(10):3.5 - something"

# Regular expression pattern to match any characters before '('
# pattern = r"^(\w+)(?=\()$"
pattern = r"(\w+\s*\w*)\(\d+\):(\d+\.\d+)"

# Use re.search() to find the match
match = re.search(pattern, s)

if match:
  # print(match)
  # If a match is found, print it
  print("Matched string: ", match.group(1))
  print("Matched string: ", match.group(2))
else:
  # If no match is found
  print("No match found.")
