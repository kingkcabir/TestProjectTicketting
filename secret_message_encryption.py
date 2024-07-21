
import string
message = input().lower()
alphabet = string.ascii_lowercase
reverse = alphabet[::-1]
cipher = dict(zip(alphabet, reverse))
encoded = "".join([cipher[letter] if letter.isalpha() else letter for letter in message])
print(encoded)