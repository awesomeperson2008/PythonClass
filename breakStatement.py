# the break keyword terminates the innermost
# loop, transferring execution to the first
# statement after the loop

while True:
    print("Enter to a number to know it is odd or even")
    print("enter 0 to break the loop")
    response = input()
    if int(response) == 0:
        print("exiting the program")
        break
    if int(response) % 2 == 0:
        print(response + " is a even number")
    else:
        print(response + " is a odd number")
