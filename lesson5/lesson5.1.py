variable_name = input()

reserved_words = [
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
    "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
]

if variable_name in reserved_words:
    print(False)
else:

    if variable_name == "":
        print(False)
    elif variable_name[0] >= '0' and variable_name[0] <= '9':
        print(False)
    else:

        has_uppercase = False
        for char in variable_name:
            if char >= 'A' and char <= 'Z':
                has_uppercase = True
        if has_uppercase:
            print(False)
        else:

            allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
            all_characters_valid = True
            underscore_count = 0

            for char in variable_name:
                if char not in allowed_characters:
                    all_characters_valid = False
                if char == "_":
                    underscore_count += 1

            if all_characters_valid:
                only_underscores = True
                for char in variable_name:
                    if char != "_":
                        only_underscores = False
                if only_underscores and underscore_count > 1:
                    print(False)
                else:
                    print(True)
            else:
                print(False)