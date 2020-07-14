def print_formatted(number):
    binary_length = len(bin(number)) - 2
    for i in range(1, number + 1):
        k = ""
        k += (binary_length - len(str(i))) * " "
        k += str(i)
        # print(k)
        k += (binary_length - len(str(oct(i))[2:]) + 1) * " "
        k += str(oct(i))[2:]
        # print(k)
        k += (binary_length - len(str(hex(i))[2:]) + 1) * " "
        # print(k)
        k += str(hex(i))[2:].upper()
        # print(k)
        k += (binary_length - len(str(bin(i))[2:]) + 1) * " "
        # print(k)
        k += str(bin(i))[2:]
        print(k)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)