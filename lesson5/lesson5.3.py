text = input("Enter your text: ")

result = ""
word = ""

for letter in text:

    if letter.isalpha():
        word += letter
    else:

        if word != "":
            result += word[0].upper() + word[1:].lower()
            word = ""

if word != "":
    result += word[0].upper() + word[1:].lower()

hashtag = "#" + result

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
