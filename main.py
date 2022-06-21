# Converts an integer to another base.
def intComponent(num, base, curr):
    if num > 1:
        curr += str(num % base)
        return intComponent(num // base, base, curr)
    return curr


# Converts the decimal part of a number to another base.
def decComponent(num, base, curr, digits=100):
    if not digits == 0 and not num == 0:
        num *= base
        curr += str(int(num))
        return decComponent(num % 1, base, curr, digits - 1)
    return curr if len(curr) > 0 else "0"


# Converts a number to a base.
def decimalToBase(num, base):
    halves = [x for x in str(num).split(".")]
    answer = intComponent(int(halves[0]), base, "")[::-1] + "."
    answer += decComponent(float("." + halves[1]), base, "")
    return answer


# Returns the index of the decimal point as well as the number formatted without it.
def getFormattedTuple(numString):
    if not numString.__contains__("."):
        numString += ".0"
    index = numString.index(".")
    numString = numString.replace(".", "")
    return numString, index


# Converts a number in a given base to decimal.
def baseToDecimal(num, base):
    total = 0
    num, index = getFormattedTuple(str(num))
    for x in [int(_) for _ in num]:
        index -= 1
        total += x * pow(base, index)
    return total


# Converts a number in a given base to another base.
def convert(num, startBase, endBase):
    num = baseToDecimal(num, startBase)
    return decimalToBase(num, endBase)


answer = convert(
    124.567,  # The number to convert
    10,  # The starting base of the number.
    2  # The ending base of the number.
)
print(answer)
