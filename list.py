itm1 = "py"
itm2 = "c"
itm3 = "c#"
itm4 = "c++"

mylist = [itm1, itm2, itm3, itm4]

print(len(mylist)-1)

print("----------------------------")

myrange = range(0, 30)

print(list(myrange))

print("----------------------------")

mycolor = ['red' ,'blue', 'green' ,'white', 'black' ,3.6]

for color in mycolor:
    if type(color) == str:
        print(f"this color is: {color}") 
    else:
        print(f"{color} is Not color")

print("----------------------------")

list1 = ['red' ,'blue', 'green' ,'white']
list1.extend(['brown', 'purple'])
print(list1)
print(len(list1))


print("----------------------------")

list1 = ['red' ,'blue', 'green' ,'white']

list1.insert(0, "add")
print(list1)

print("------------clear----------------")

list33 = ['red' ,'blue', 'green' ,'white']
list33.clear()
print(list33)


print("----------------------------")

list1 = ['red' ,'blue', 'green' ,'white']
list1.pop()
print(list1)


print("----------------------------")


list1 = ['red' ,'blue', 'green' ,'white']
list1.remove('red')
print(list1)