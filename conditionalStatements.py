# If Expression
# if expr:

if True:
    print("it is true")
else:
    print("it is false")

if False:
    print("it is false")
    print("print intented next line")
else:
    print("it is not false")

if bool("python"):
    print("it is python")
else:
    print("it is not python")

h = 50

if h > 50:
    print("h is not greater than 50")
else:
    print("h is less than or equal to 50")
    if h < 20:
        print("h is less than 20")
    else:
        print("h is between 20 and  50")

#elif
if h > 50:
    print("h is not greater than 50")
elif h < 20:
    print("h is less than 20")
else:
    print("h is between 20 and  50")



