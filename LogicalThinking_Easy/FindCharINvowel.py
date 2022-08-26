"""This python program will involve the use of an array which stores all vowels and then deploy an if-else loop
condition to determine whether the input character is a vowel or a consonant. """

def isVowelorConstant(char):

    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    if char in vowel:
       print("Vowel")
    else:
       print("Constant")


if __name__ == "__main__":

    print("Is Vowel: ")
    char = input()
    isVowelorConstant(char)
