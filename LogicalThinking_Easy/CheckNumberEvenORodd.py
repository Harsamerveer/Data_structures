def evenorodd(num):
    if num%2 == 0:
       print("Number is Even")
    else:
       print("Number is Odd")


if __name__ == "__main__":

    print("Please Input a number to check if odd or even : ")
    num = int(input())
    evenorodd(num)
