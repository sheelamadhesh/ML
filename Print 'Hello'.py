"""
a= 10 #integer
b= 20.45 #float
c= a+b #float is result
print (a+b) #print

#print (c)  # multiline command

name ="My name is Sheela. Sheela ji Javani " # string
print (name)
a = True #bool
print (a)
str = '\"Hello\"' # to print String alongwith "
print (str) 

My_wish = "Learn ML along with \"Python\" fast"
print (My_wish)
import constants
print (constants.no_of_days)
floor_value = -12//5

add = 10
#add = add + 20
print (add)
print (id(add))

add =+ 10
print (add)
add += 10
#print (floor_value)
print (add)

sub = 10
print (sub)
sub -= 20
print(sub)
sub =- 10
print (sub)

#Logical Operators
y =20
name = "Alice"
my_name = 'sheela'
print ("is y > 30 = ", y>30 or y >0)   # > operator
print ("S in my name : " ,'S' in my_name ) # in operator
print (" not operator" , not y==20)

# is Operator - check whether both variables are pointing to same object
a = 10
print (id(a)) 
c = 10
print (id(c)) # when value is same , both variables points to same memory location
b = 20
print (id(b))
b = a # while assigning value of a to b , b points to a's memory address
print (id(a) ,id(b))
#add =+ 10 # add = 0+ 10
add += 10 # add = add+ 10
print (add)
print (id(add))
add += 10 # add = add+ 10
print (add ,id(add))
print (type(add))
d = 3.14
print (type(d))

#Input function
40
my_age = input("Enter your age :")
print (type(my_age))
my_age = int(my_age)
print (type(my_age))
my_name = input ("Enter your name :")
print (type(my_name))
#my_name = int(my_name) # Invalid value error
pritnt (my_name)

impor sys
import datetime

age = input ("Enter your age:")
current_date = datetime.date.today()
year_of_birth = current_date.year - int(age)
print (year_of_birth)

a= 4
b = 5
if a == b:
    print ("a is equal to b")
elif ( a > b):
    print ("a is greater than b")
elif (b>a):
    print ("b is greaterb than a")
else:
    print ("???")
    
for i in range(1,11):
    for j in range(1,i+1):
        print ("*",end="")
    for k in range(1,11-i):
        print (" ",end="")
    print()

#While loop
counter=1
second_counter = 1
while (counter <= 11):
    print ("+",end ="")
    while (second_counter <= counter):
        print (" ",end ="")
        second_counter = second_counter + 1
        print()
    counter =counter+ 1
   

numbers = ["s","h"]
for i in numbers:
    print(i)

a = [10,15,15,20,25,30]
print( a[1])
print (a)
b = a[3:5] #slice list and create new list by copying 3 to 5 index of list b
print (b)
b[0] = 25 # assign 25 to first element of list b
print (b)
a.append(35) # append value 35 in the end of list a
print (a)
print (a)
b.remove(25)
print (b)
a.pop() # removes last value (last index)
print(a)
a.remove(10) # remove value 10 from list a
print(a)
a.extend(b) #extend list a by appending b list in the end
print(a)
a.sort() #sort
print(a)
a.sort(reverse=True) #sort in reverse order
print(a)
del a[3:5] #del index 3 to 5 of list a
print(a)

# Creating list with loop control iteration
cube_list = [x**3 for x in range (7)]
print (cube_list)
cube_list = [x**3 for x in range (7) if x%2 ==0 ]
print (cube_list)
cube_list = [x**3 if x%2 ==0 else 10 for x in range (7) ]
print (cube_list)

#Two sum
nums =[2,7,11,15]
target = 9
#nums =[3,2,4]
#target = 6
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        sum = nums[i] + nums[j]
        if sum == target:
            print(i,j)
        else:
            print(-1,-1)

nums =[1,2,3,1]
for i in range(len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i] == nums[j]:
            print (True)
        else:
            print (False)
for num in nums:
    if nums.count(num) > 1:
        print (True)
    else:
        print (False)


wish = "loveSheela,I love tea"
print (wish[1:6]) # end indexes is exclusive

#Pivot
nums =[1,7,3,6,5,6]
sum_right = 0
sum_left = 0
for i in range(len(nums)):
    if i > 0:
        sum_left = sum_left + nums[i-1]
        sum_right = 0
    for j in range(i+1,len(nums)):
        
        sum_right = sum_right+ nums[j]
          
        if sum_right == sum_left:
            print (nums[i-1])
        else:
            continue

#intersection
#nums1 =[1,2,2,1]
#nums2 = [2,2]
nums1 =[4,9,5]
nums2 = [9,4,9,8,5]
result = []
for num1 in nums1:
    for num2 in nums2:
        if (num1 == num2) and (num1 not in result):
            result.append(num1)
            print(result)
        else:
            continue

#Reverse of string
#String = "The Sky is blue"
String = "  Hello World  "
rev = String[::-1]
print(rev)
a = []
b = []
a = (String.strip()).split(" ")
#a = String.split(" ")    
b.append(" ".join(reversed(a)))
print (a)
print (b)
print(len(a))

#Find the first occurance
haystack = "sadbutsad"
needle ="sado"
if(haystack.find(needle,0)) >= 0:
    print (haystack.find(needle,0))
else:
    print (-1)

nums = [50, 35, 78, 66, 17]
nums.reverse()
print (nums)

def reverse_array(nums):
    nums.reverse()
    return [nums]

nums = [50, 35, 78, 66, 17]
reverse_array(nums)

nums= [2, 4, 5, 6, -1]
element = 3
position = 5

def insert_element_at_position(nums, element, position):
   
    nums.insert(position-1,element)
    nums2= nums[0:len(nums)-1]
    return nums2

nums3 = insert_element_at_position (nums, element, position)
print (nums3)
   

   #intersection
#nums1 =[1,2,2,1]
#nums2 = [2,2]
nums1 =[4,9,5]
nums2 = [9,4,9,8,5]
result = []
for num1 in nums1:
    for num2 in nums2:
        if (num1 == num2) and (num1 not in result):
            result.append(num1)
            print(result)
        else:
            continue

a = [4, 2, 2, 3, 1]
b = [2, 2, 2, 3, 3]
def get_intersection_with_maintained_frequency(a, b):
   result = []
   for i in a:
    for j in b:
        if (i == j) and (i not in result):
           result.append(i)
        elif i == j and (i in result):
           freq_i = a.count(i) 
           freq_j = b.count(j) 
           freq_i_in_result = result.count(i)
           if ((freq_i <= freq_j) and (freq_i > freq_i_in_result)):
              result.append(i)                              
           elif ((freq_j <= freq_i) and (freq_j > freq_i_in_result)):
              result.append(i) 
           else:
              continue
   return result
c = get_intersection_with_maintained_frequency (a,b)
print (c)

result = []
for i in a:
    for j in b:
        if (i == j) and (i not in result):
            result.append(i)
        elif i == j and (i in result):
            freq_i = a.count(i) 
            freq_j = b.count(j) 
            freq_i_in_result = result.count(i)
            if ((freq_i <= freq_j) and (freq_i > freq_i_in_result)):
                result.append(i)                              
            elif ((freq_j <= freq_i) and (freq_j > freq_i_in_result)):
                result.append(i) 
            else:
                continue
return result



#Pivot
numbers =[1, 2, 3, 4, 5, -15, 7]
def get_pivot_index(numbers):
    sum_right = 0
    sum_left = 0
    
    for i in range(len(numbers)):
        sum_left = sum(numbers[0:i])
        sum_right = sum(numbers[i+1:])
        if sum_left == sum_right:
            return i
        elif i == len(numbers):
            return -1
        else:
            continue
        
c = get_pivot_index(numbers)
print (c)

s= "best technical interview prep courses"
def reverse_words(s):
    a = (s.strip()).split(" ")     
    b = " ".join(reversed(a))    
    return b
c = reverse_words(s)
print (c)

"""

def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
   
    # Write your code here.
    count =0
    for char in s:
        if char.isalpha():
            count +=1
    
    return count

s = "InTerView"
def uppercase_to_lowercase(s):
   
    # Write your code here.
    s.lower()
    return s.lower()

print(uppercase_to_lowercase(s))


sentence =" Hello World "
def length_of_last_word(sentence):
  
    # Write your code here.
   
    lists = (sentence.strip()).split(" ")
    return len(lists[-1])

print(length_of_last_word(sentence))
"""
a = [1, 2]
print(a * 3)
