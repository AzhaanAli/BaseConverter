# Converts an integer to another base.
def intComponent(num, base, curr):
    if num < 1:
        return curr
    else:
        curr += str(num % base)
        return intComponent(num // base, base, curr)


# Converts the decimal part of a number to another base.
def decComponent(num, base, curr, digits):
    if digits == 0 or num == 0:
        return curr
    else:
        num *= base
        curr += str(int(num))
        return decComponent(num % 1, base, curr, digits - 1)


# Converts a number to a base.
def decimalToBase(num, base, digits):
    halves = [x for x in str(num).split(".")]
    answer = intComponent(int(halves[0]), base, "") + "."
    answer += decComponent(float("." + halves[1]), base, "", digits)
    return float(answer)


# Converts a number in a given base to decimal.
def baseToDecimal(num, base):
    num = str(num)
    if not num.__contains__("."):
        num += "."
    index = num.index(".")
    num = num.replace(".", "")
    total = 0
    for x in [int(_) for _ in num]:
        index -= 1
        total += x * pow(base, index)
    return total


# Converts a number in a given base to another base.
def convert(num, startBase, endBase, digits):
    num = baseToDecimal(num, startBase)
    return decimalToBase(num, endBase, digits)


print(convert(11110001101.101011, 2, 4, 100))
