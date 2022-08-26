"""This program calculates the factorial of the input number using recursion including explanation."""

def fac(num):
    i = num
    check = 0
    result = 1
    while i != check:
        result = result * i
        i -= 1
    print(result)

if __name__ == "__main__":

    print("Number: ")
    n = int(input())
    fac(n)