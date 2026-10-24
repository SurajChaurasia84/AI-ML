# Ask the user for a string and check whether it is a palindrome or not.

text = input("Enter a string: ")

# Manually reverse the string using a loop
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

if text.lower() == reversed_text.lower():
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")