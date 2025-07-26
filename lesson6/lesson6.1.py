import string

letters = string.ascii_letters
text = input("Enter two letters with a dash (like a-f): ")
start_letter, end_letter = text.split("-")

start_index = letters.index(start_letter)
end_index = letters.index(end_letter)

result = letters[start_index:end_index + 1]
print(result)