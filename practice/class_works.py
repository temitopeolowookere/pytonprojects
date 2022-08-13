import string


word = input(" what would you like to encode")
key = int(input(" your key? "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

lower_letters_code = lower_letters[key:] + lower_letters[:key]
upper_letters_code = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters
letters_code = lower_letters + upper_letters_code

print(letters)
print(code)