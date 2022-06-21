# Converts an integer to another base.
def intComponent(num, base, curr):
    if num >= 1:
        curr += str(num % base)
        return intComponent(num // base, base, curr)
    return curr


# Converts the decimal part of a number to another base.
def decComponent(num, base, curr, digits):
    if not digits == 0 and not num == 0:
        num *= base
        curr += str(int(num))
        return decComponent(num % 1, base, curr, digits - 1)
    return curr


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


print(intComponent(124, 3, ""))
