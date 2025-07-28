import keyword
import string

variable_name = input()

if (
    variable_name in keyword.kwlist
    or variable_name == ""
    or variable_name[0].isdigit()
    or any(c.isupper() for c in variable_name)
    or any(c in string.punctuation.replace("_", "") for c in variable_name)
    or any(c.isspace() for c in variable_name)
    or (variable_name.count("_") > 1 and set(variable_name) == {"_"})
):
    print(False)
else:
    print(True)