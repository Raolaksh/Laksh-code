name = "laksh"
print(name)
'''
laksh is a good boy 
'''
print(name[0])
print(name[2:4])
# if i write a command like shown above it will take 2,3 not 4th.
# if i write 2:5 it will take 2,3,4 not 5th

print(name)
print(name.strip())
print(len(name))

var = name.upper()
var = name.replace("l","D")
print(var)

name = "harry","laksh","agrim"
# var = name.replace(",",'\n')
print(var)

stri = "this is "
name1 = "laksh"
name2 = "harry"
stri2 = "this is not a"
# print(stri + name)
# you can uncomment it if you want
# temp = "this is {0} and he is a good boy named {1}".format(name1,
# name2)
# if you want that it will say that this is harry and he is a good boy named laksh you can replace the numbers like at place of 0 you write 1 and baki tum samajdar.
temp = f"this is {name2} and he is a good boy {name1}"
print(temp)

# Quiz Questions:
# 1. ** exponentation
# 2. // floor division operator
# 3. % modulo operator

a = 33
b = 10
c = 82

print(a**b)
print(c//a)
print(b%c)
