# ------------------------------------------------------- #
# Conversion methods.

# Converts an integer to another base.
def int_component(num, base, curr=""):
    return curr if num == 0 else int_component(num // base, base, curr + str(num % base))


# Converts the decimal part of a number to another base.
def dec_component(num, base, curr="", digits=100):
    if digits == 0 or num == 0:
        return curr if len(curr) > 0 else "0"
    x = num * base
    return dec_component(x % 1, base, curr + str(int(x)), digits - 1)


# Converts a number to a base.
def decimal_to_base(num, base):
    halves = [x for x in str(num).split(".")]
    return int_component(int(halves[0]), base)[::-1] + "." + dec_component(float("." + halves[1]), base)


# Returns the index of the decimal point as well as the number formatted without it.
def get_formatted_tuple(num_string):
    if not num_string.__contains__("."):
        num_string += ".0"
    return num_string.replace(".", ""), num_string.index(".")


# Converts a number in a given base to decimal.
def base_to_decimal(num, base):
    total = 0
    num, index = get_formatted_tuple(str(num))
    for x in [int(_) for _ in num]:
        index -= 1
        total += base ** index * x
    return total


# Converts a number in a given base to another base.
def convert(num, start_base, end_base):
    num = base_to_decimal(num, start_base)
    return decimal_to_base(num, end_base)


# ------------------------------------------------------- #
# User-input methods.


# Prints a message and returns the users reply.
def prompt(message):
    return input(message + ": ")


# Prompts the user for various data-types.
def prompt_float(message="Enter a decimal"):
    return float(prompt(message))


def prompt_integer(message="Enter an integer"):
    return int(prompt(message))


# ------------------------------------------------------- #
# Method calls.

# Prompt the user for important information.
beginning_number = prompt_float("Enter a number to convert")
base_start = prompt_integer("In what base is this number?")
base_end = prompt_integer("Which base do you wish to convert to?")
# Compute and print the number in the desired base.
converted = convert(beginning_number, base_start, base_end)
print("{0} is your number in base {1}".format(converted, base_end))
