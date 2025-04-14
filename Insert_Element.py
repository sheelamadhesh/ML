# Insert an element
#def insert_element_at_position(nums, element, position):
"""
{
"nums": [2, 4, 5, 6, -1],
"element": 3,
"position": 2
}
"""
nums =[2, 4, 5, 6, -1]
element = 3
position = 2
num2 = []

#iterate  current list and write elements into new list based on given data
for i in range (len(nums)):
    if i < (position-1):
        num2.append(nums[i])
    elif i == (position-1):
        num2.append(element)
    elif i >=position and i <=(len(nums)-1):
        num2.append(nums[i-1])
print (num2)   
#shift index from their current index to one index forward
for i in range ((len(nums)-1),position-1 , -1):
    nums[i] = nums[i-1]

nums[position-1] = element
print (nums)

import sys
print(sys.executable)
import numpy
print(numpy.__version__)