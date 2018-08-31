num1 = input('Enter any number : ')
try:
    val = int(num1)
    if num1 == str(num1)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")
