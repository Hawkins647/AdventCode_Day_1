# part 1

def get_first_last_number(lines):
    digits = []
    for text in lines:
        first_digit = ""
        last_digit = ""
        for char in text:
            if char.isnumeric() and first_digit == "":
                first_digit = char
            elif char.isnumeric():
                last_digit = char

        if (first_digit == "" or last_digit == ""):
            digits += [(first_digit + last_digit) * 2]
        else:
            digits += [first_digit + last_digit]

    return digits


with open ("stuff.txt", "r") as file:
    lines = file.readlines()

digits = get_first_last_number(lines)
print(digits)
total = 0
for val in digits:
    total += int(val)

print(total)





