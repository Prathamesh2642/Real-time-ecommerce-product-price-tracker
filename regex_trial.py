import re

# Your input text
input_text = "/search?q=casio+watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2"

# Define the regex pattern
pattern = r'page=(\d+)'

# Search for the pattern in the input text
matches = re.findall(pattern, input_text)

# Print the matches
print(matches)