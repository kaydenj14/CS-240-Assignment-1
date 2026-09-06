base = 10
binary = 1010


# Binary to number converter

def binaryToNum(binary):
    num = 0
    numberInString = str(binary)
    for char in numberInString:
            num = (num * 2) + int(char)
    print(num)

binaryToNum(binary)

# number to binary converter

def numbertoBinary(base):
    if base == 0:
        return 0

    binary_string = ""

    while base > 0:
        remainder = base % 2
        binary_string = str(remainder) + binary_string
        base = base // 2

    print(binary_string)


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

    print(binary_string)

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


print(numberToHexadecimal(45))