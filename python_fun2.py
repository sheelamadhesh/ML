tuple_1 = ('max',28,'newyork')
print(tuple_1)
tuple_2 = 'max',28,'newyork'
print(tuple_1)
#tuble unpacking
person =("sheela",40,"chennai")
name,age,city = person
print (name,age,city)
#tuple cannot be declared as tuple when there is only one element to it
tuple_3 = (5)
print(tuple_3)
print(type(tuple_3))
#tuple defination when only one element is there
tuple_4 = (18,)
print (tuple_4)
print(type(tuple_4))
#iterate through tuple
for item in tuple_1:
    print(item)
#iterate through range
for i in range(len(tuple_1)):
    print (i,tuple_1[i])
#iterate through tuple using enumerate
for idx, val in enumerate(tuple_1):
    print(idx,val)
#search a tuple
if "newyork" in tuple_1:
    print (True)
#count of value
tuple_5 = (1,2,3,4,4,6)
tuple_5.count(4)
print (tuple_5.count(4))
#index of value
print (tuple_5.index(4))
#converting list to tuple using builtin function
tuple_6 = tuple([1,4,6,8,9])
print (type(tuple_6),tuple_6)
#convert string to tuple
tuple_7 = tuple("hello")
print(tuple_7)
#convert tuple to list
my_list = list(tuple_7)
print (type(my_list),my_list)
#memory size
import sys
print(sys.getsizeof(my_list),bytes)
print(sys.getsizeof(tuple_7))
# tuple returns multiple values
def divide (a,b):
    quotient = a//b
    reminder = a % b
    return (quotient,reminder)

result = divide(10,3)
print (type(result),result)

#tuple values assigned to two variables
def divide (a,b):
    quotient = a//b
    reminder = a % b
    return quotient,reminder

quo,rem = divide(10,3)
print (type(quo),quo,type(rem),rem)


#Sets

set1 = {1,5,10,6}
print(type(set1),set1) #set
print(max(set1)) #10
#define an empty set
set3 =set() #set()
print (type(set3))
#set element cant be accessed 
#print (set1[1])
#sets removes depulicates automatically
set4 = {1,1,1,2,2,0,6,7,9,10,10}
print (set4) # ans:{1, 2, 4, 6, 7, 9, 10}
print (set4) # ans:{1, 2, 4, 6, 7, 9, 10}
#add & remove
fruits = {"a","b","c","d"}
fruits.add("f")
fruits.remove("c")
#fruits.remove("z") #key error
#Set operations
#union AUB
more_fruits = {"A","B","C","a"}
all_fruits = fruits.union(more_fruits)
print (all_fruits)
#intersection A intersection B
common_fruits = fruits.intersection(more_fruits)
print (common_fruits)
#difference (AUB-AinterB)
different_fruits = all_fruits.difference(common_fruits)
print(different_fruits)
#Update works like extended set
fruits.update(more_fruits)
print (fruits)
#Discard - remove item. no error when no items matchs
fruits.discard("a")
print (fruits)
#clear
common_fruits.clear()
print(common_fruits)
# Issubset & issuperset
setA ={1,2,3,4,5,6}
setB = {1,2,3,6}
print(setA.issubset(setB)) #false
print(setA.issuperset(setB)) #ture
print(setB.issubset(setA)) #true
print(setB.issuperset(setA)) #false
#isdisjoint(setx): true if both sets have a null intersection
setC ={7,8}
print(setA.isdisjoint(setC))

#Leetcode 217
nums1 = {1,1,2,4}
nums2 = {1,2,3}

def containsDuplicate (nums):
    return len(nums) != len(set(nums))

nums1 = {1,1,2,4}
nums2 = {1,2,3}
print(containsDuplicate(nums2))

# Intersection
def intersection(nums1,num2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    intersection_set = set_nums1.intersection(set_nums2)
    return intersection_set

print (intersection(nums1,nums2))

#Dictionaries
captial_city = {"Nepal":"kathmandu","Italy":"Rome","England":"London"}
print(captial_city)
print (captial_city["Nepal"])
#adding new key & value
captial_city["Japan"] = "Tokyo"
print(captial_city)
#Keys of dic
key = captial_city.keys()
print (key)
val = captial_city.values()
print (val)
items = captial_city.items()
print (items)
#Removing items
print (captial_city.pop("Nepal")) # value will be returned when removed
print(items)
del captial_city["England"]
print(items)
#Membership test for dic
square_dic = {1:1,2:4,3:9,4:16,5:25,6:36,9:49}
print(1 in square_dic)
print(7 in square_dic)
print(49 in square_dic)
print(49 in square_dic.values())
#Iterating through dictionary
for keys in square_dic:
    print (keys,square_dic[keys])

for key in square_dic.keys():
    print ("key:",key)
for value in square_dic.values():
    print ("val:",value)
for item in square_dic.items():
    print ("item:",item)

#use numbers as key but more careful
#retrive key
print (square_dic[3]) 
#retrive index
#print (square_dic[0]) # Error
#use of tuple with immutable elements
my_tuple = (8,7)
square_dic[my_tuple] = 64
print(square_dic)
#use of list 
my_list = [10]
#square_dic[my_list] = 100 # type error
print(square_dic)
#using a dic for find no of occurance 
numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
counts ={}
for num in numbers:
    if num in counts:
        counts[num] +=1
    else:
        counts[num] =1
print (counts)
#Sum
nums = [2,3,1,7,11,15]
target = 9
def twosum (nums,target):
    dict = {}
    for i in range(len(nums)): # 0,1,2,3,4,5
        dict[nums[i]] = i # 2:0->2:1->2:2->7:3->11:4->15:5
        print (dict.items())
        for num in nums: #2,2,2,7,11,15
            diffence = target - nums[i] # 7->7->7->2->4->8
            if diffence in dict and dict[diffence] != i: #7 in dic and 7's value i.e index is not 0
               return dict.items(),i,dict[diffence]
print ("twosum",twosum (nums,target))

# Builtin
import math
x=math.atan(10)
y=math.factorial(3)
z=math.floor(-3.2)
print(x,y,z)
import random
print(random.randint(1,10))
#user defined function
#import user_defined_module as udm
#udm.find_square(2)
#from user_defined_module import find_square # importing required function 
#Lambda function
def print_hi():
    print("hi")

print_hi()

print_hi1 = lambda : print ("Hi1")
print_hi1()
print_hi2 = lambda name : print ("Hi "+name+"!")
print_hi2("Sheela")
print ((lambda x: x + x)(2)) #4
c = lambda x: x + x 
print (c(3))

func = lambda a,b :(

    b-a if a <=b else a*b
)

print (func(10,12))
#map()
def square (num):
    return num*num
def double (num):
    return num + num
funcs = (square,double)
nums = [1,2,3,4,5,6,5,6]
number_square_list = list(map(square,nums))
number_square_set = set(map(square,nums))
number_lamda_square = list(map(lambda x:x*x , nums))
number_lamda_function_par = list(map(lambda x:x(10)  ,funcs)                 )
print (number_square_list)
print (number_square_set)
print (number_lamda_square)
print (number_lamda_function_par)
#write a code to suare all numbers
nums =[1,2,3,4,5]
results = list(map(lambda x: x*x , nums))
print (results)
#filter
def over_75 (age):
    return age >= 75
ages = [56,67,78,85,90,100]
over_75 = (filter(over_75,ages))
print(type(over_75),list(over_75))

less_than_zero = list(filter(lambda x:x < 0 ,list(range(-5,5))))
print (less_than_zero)
less_than_zero = list(map(lambda x:x < 0 ,list(range(-5,5))))

print (less_than_zero)

numbers =[1,2,3,4,5,6,7,8]
even_numbers = list(filter(lambda x:x%2 ==0 ,numbers))

print(even_numbers)
# code to keep vowels
letters = ['a','b','c','d','e','f','i','o','u']
vowels =['a','e','i','o','u']

vowels_only = list(filter(lambda x: x in vowels ,letters))
print(vowels_only)