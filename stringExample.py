#String - Immutable sequence of unicode
#\n - Is a universal new line character. In Windows, no need to add
#\n\r. Just \n will take care

multiline = "This is a python program.\nPython is a dynamic object oriented language"
print(multiline)

escape = "This string has \"double quote\" in it."
print(escape)

#Raw string
path = r'C:\User\python'
print(path)

#String constructor
strValue = str(3000)
print(strValue)
strDouble = str(2.312987e90)
print(strDouble)

#Type function
s= "Python"
print(s[3])
print(type(s[4]))

# Help method
print(help(str))

c = "all lower"
print(c.capitalize()) #String is immutable, creates new string
print(c)    # old string unchanged
