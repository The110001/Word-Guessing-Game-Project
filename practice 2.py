# practice 2
# calculate the multiplication and sum of two numbers
print("hello there! in order to make our little program work here, you need to provide two numbers.")

while True:
    print("")
    number1 = input("1/ please provide the first number here: ")
    number2 = input("2/ please provide the second number here: ")

    if number1.isdigit() and number2.isdigit():
        print("")
        print("thank you for the inputs")
        if int(number1) * int(number2) <= 1000:
            print("the multiplication of the two numbers that you provided are ", int(number1) * int(number2))
        else:
            print("the sum of the numbers provided are ", int(number1) + int(number2))
    else:
        print("")
        print("the inputs provided do not follow the guid-lines. please try again.")