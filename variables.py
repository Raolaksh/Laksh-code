a = 4
x = "laksh"
c = 45.32
#if we did't put the double quotes it will give us a error because it will thought that it is a variable but we haven't made any variable so we have to put double quotes then python will say that ohhh it is a string jane do jane do

print(a + c)
print(a - c)
print(a * c)
print(a / c)

# wrong syntax
# laksh project
# rules for creating variables

# 1. variable should start with only a letter or an underscore
# 2. variable cannot start with a number
# 3. it can only contain alpha numeric characters
# 4. variable names are case sensitive. that means that laksh and Laksh are two different variables.
# 5. variable kya hota ha ek dabba hota ha in which you can put number or a string and also a python project

# type is a function which can tell which type of variable is a or b or anything else.

typeA = type(a)
print(typeA)

# if i type that a = 31 here 31 is a number and if  i write a = "31" here 31 is a string.

a = 31
print(type(a))
print(a + 2)

# up here if i have written a = "31" and under it i say a + 2 so it is an error because we can't add integer in a string here type is used to find out what type of file it is .
# if i write that 3.24 here it is a float variable .
# int is integer.
e = int(31)

e = 33
e = float(e)
print(e + 2)
# this is called type casting.
