# Converts an integer to another base.
def int_component(num, base, curr):
    if num > 1:
        curr += str(num % base)
        return int_component(num // base, base, curr)
    return curr


# Converts the decimal part of a number to another base.
def dec_component(num, base, curr, digits=100):
    if not digits == 0 and not num == 0:
        num *= base
        curr += str(int(num))
        return dec_component(num % 1, base, curr, digits - 1)
    return curr if len(curr) > 0 else "0"


# Converts a number to a base.
def decimal_to_base(num, base):
    halves = [x for x in str(num).split(".")]
    answer = int_component(int(halves[0]), base, "")[::-1] + "."
    answer += dec_component(float("." + halves[1]), base, "")
    return answer


# Returns the index of the decimal point as well as the number formatted without it.
def get_formatted_tuple(num_string):
    if not num_string.__contains__("."):
        num_string += ".0"
    index = num_string.index(".")
    num_string = num_string.replace(".", "")
    return num_string, index


# Converts a number in a given base to decimal.
def base_to_decimal(num, base):
    total = 0
    num, index = get_formatted_tuple(str(num))
    for x in [int(_) for _ in num]:
        index -= 1
        total += x * pow(base, index)
    return total


# Converts a number in a given base to another base.
def convert(num, start_base, end_base):
    num = base_to_decimal(num, start_base)
    return decimal_to_base(num, end_base)


# Prints a message and returns the users reply.
def get_user_input(message):
    return input(message + ": ")


# Prompts the user for various data-types.
def get_float_input(message):
    return float(get_user_input(message))


def get_integer_input(message):
    return int(get_user_input(message))


# Prompt the user for important information.
beginning_number = get_float_input("Enter a number to convert")
base_start = get_integer_input("In what base is this number?")
base_end = get_integer_input("Which base do you wish to convert to?")
# Compute and print the number in the desired base.
converted = convert(beginning_number, base_start, base_end)
print("{0} is your number in base {1}".format(converted, base_end))
