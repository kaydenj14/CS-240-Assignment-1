base = 10
binary = 1010


# Binary to number converter

def binaryToNum(binary):
    num = 0
    numberInString = str(binary)
    for char in numberInString:
        num = (num * 2) + int(char)
  #  print(num)

binaryToNum(binary)

# number to binary converter

def numbertoBinary(base):
    if base == 0:
        return "0"


    binary_string = ""

    while base > 0:
        remainder = base % 2
        binary_string = str(remainder) + binary_string
        base = base // 2

    return binary_string


numbertoBinary(base)


#Octal

def numbertoOctal(base):
    if base == 0:
        return 0

    binary_string = ""

    while base > 0:
        remainder = base % 8
        binary_string = str(remainder) + binary_string
        base = base // 8

    return binary_string

numbertoOctal(base)

#hexadecimal

def numberToHexadecimal(number):
    if number == 0:
        return "0"

    hexadecimal_string = ""
    digits = "0123456789ABCDEF"

    while number > 0:
        remainder = number % 16
        hexadecimal_string = digits[remainder] + hexadecimal_string
        number = number // 16

    return hexadecimal_string



UNSIGNED_MAX = (2 ** 32) - 1
SIGNED_MIN = -(2 ** 31)
SIGNED_MAX = (2 ** 31) - 1

print("Unsigned max:", UNSIGNED_MAX)
print("Signed min:", SIGNED_MIN)
print("Signed max:", SIGNED_MAX)

print("Zero in binary:", numbertoBinary(0))
print("Zero in hexadecimal:", numberToHexadecimal(0))

print("Unsigned max in binary:", numbertoBinary(UNSIGNED_MAX))
print("Unsigned max in hexadecimal:", numberToHexadecimal(UNSIGNED_MAX))


negative_number = -10
twos_complement = (2 ** 32) + negative_number

print("Negative number:", negative_number)
print("Two's complement in binary:", numbertoBinary(twos_complement).zfill(32))
print("Two's complement hexadecimal:",numberToHexadecimal(twos_complement).zfill(8))