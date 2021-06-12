def print_formatted(number):
    length = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        string = str(i).rjust(length) + ' ' + str(oct(i))[1:].rjust(length) + ' ' + str(hex(i))[2:].upper().rjust(length) + ' ' + str(bin(i))[2:].rjust(length)
        print(string)

