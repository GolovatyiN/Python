import string

text = input("Enter your text: ")
text = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in text)

words = text.split()
capitalized = ''.join(word.capitalize() for word in words)
hashtag = "#" + capitalized

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
