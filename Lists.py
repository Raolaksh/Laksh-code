'''
python collections:
1. List
2. Tuple
3. Set
4. Dictonary
'''

lst = [61,2,3,4,6,41]
var = type(lst)
lst[2] = 45
lst.append(101)
# lst.insert(1,151)
var = lst
# var = lst[1:4]
lst.remove(6)
lst.pop()
'''
 pop function will remove the last number of the list.
 del will remove any number which you say just you have to write its index.
 you also can delete entire list by using del function.
 by writing del lst entire list will gayab.
 there is a anothor function which will clear your list lst.clear().
'''
del lst[3]
print(var)

# tuple:
a =("harry","rohan","shubh")
var = a
var = type(a)
# cannot do this because tuple list cannot be changed
# a[0] = "vikrant"
# you canot change tuple list but you can change the tuple to list then do changes you want command-a = list(a).
print(var)

# SET:

s1 = {23,3,3,22,3,22,3,2,2,2,31,5,46,5,6,7}
# if you want to know what is this uncomment it and run it
# s1.add(44444)
# s1.update([12,12,423,3423,345,654,67,457])
print(len(s1))
# in the below statement i have given a number which is in the list if i give a number
# is not in list it will give me an error thats why i used discard 
# there are many list functions like  .pop , .clear , del , 
# and.....intersection , union
s1.remove(2)
s1.discard(1557)
print(s1)

LakshDict = {
    "name": "laksh",
    "class": "8th",
    "marks": 88.5,
    "hours in school": 6
}
print(LakshDict["hours in school"])
LakshDict["marks"] = 70
LakshDict.pop("marks")
# del,clear,pop,update you can ue these functions 
print(LakshDict)