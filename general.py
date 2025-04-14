print("hihihello\r youdidyesimfine")
print("hello\n you")
print('A', 'B', sep='*', end=' ')
print('C')

a = 4/2+2**1
a = 4//3 
a = 1-2//3+4
a= 3**0
a = 1+1//2*3
a= 0 % 2
print (a)
#floor = float(input("Enter float number:"))
#print(floor)

for i in range(1,2):
    print(i, end=' ')
else:
    print('FINISHED')

# break inside for
for i in range(3):
    if i == 1:
        break
    print(i, end=' ')
else:
    print('FINISHED')

# continue inside for

for i in range(4):
    if i % 2 == 1:
        continue
    print(i, end=' ')
else:
    print('FINISHED')
others = -1
for i in range (1,3):
    for j in range(1,2):
        if i == j:
            others =+ 1
    else:
        others += 1
else:
        others += 1
print(others)

print((1,2,3)[4:5])

the_list = [0, 1, 2, 3]
print(the_list[-3:-1])

list_a = [1]
print(id(list_a))
print(list_a)
list_b = list_a
print(id(list_b))
print(list_b)
list_b[0] = 0
print(list_b)
print(id(list_b))
print(list_a[0] == list_b[0])
print(list_a[0],list_b[0])
print(list_a,list_b)

list_a = [1]
print(list_a)
print(id(list_a))
list_b = list_a[:]
print(list_b)
list_b[0] = 0
print(list_b)
print(id(list_b))
print(list_a[0] == list_b[0])

the_list = [1]
print(the_list)
the_list.append(2)
print(the_list)
the_list.insert(0, 0)
print(the_list)

the_list = [1,2]
del the_list[0]
print(the_list)

String = "abc"
print(String)
print (String[0])
#String[0] ="c" #Typeerror - String is immuatable
print(String)

empty_tuple = () # tuple() has the same meaning
print(empty_tuple)
#one_element_tuple = tuple(1) # must not be replaced with (1)!
#print(one_element_tuple)
one_element_tuple = 1, # the same effect as above
print(one_element_tuple)
two_element_tuple = (1, 2.5)
print(two_element_tuple)
two_element_tuple = 1, 2.5 # the same effect as above
print(two_element_tuple)
tuple = (1, 2.2, '3', True)
print(type(tuple))
