list1=[1,2,3,4,5,6,4,5,6,1,3,]
list2=['apple',"bannan","cherry","orange"]

print(list1)
print(list2)

##append

list1.append(20)
list1.append(21)
list1.append(22)
list2.append("coca")
list2.append("lime")


print(list2)
print(list1)

##copy

x=list1.copy()
x1=list2.copy()
print(x1)
print(x)

##count()

print(list1.count(3))
print(list1.count(2))
print(list2.count("apple"))
y=list1.count(4)
print(y)

##extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
list1.extend(list2)
print(fruits)
print(list1)

##index

x = fruits.index("cherry")
print(x)

##pop

list1.pop(2)
list1.pop(4)

print(list1)
print(list1)

##remove

fruits.remove("cherry")

print(fruits)


fruits.reverse()
print(fruits)


