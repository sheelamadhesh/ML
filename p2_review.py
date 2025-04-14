
#Sum
numbers = [-7, -6, 0, 7, 8, 9, 10]
target = 0

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    """
    found_match = False
    minimum = numbers[0]
    maximum = numbers[len(numbers)-1]
  
    
    for i in range (len(numbers)):
        difference = target - numbers[i]
        if difference in numbers:
            found_match = True
            return [i,numbers.index(difference)]
    
    return [-1,-1]


    j = len(numbers)-1
    i = 0
    while(i<j):
        sum = numbers[i]+ numbers[j]
        if sum ==target:
            return [i,j]
        elif sum > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]

        

print (pair_sum_sorted_array(numbers, target))
"""
import math
nums = [3, 3, 3, 2, 2, 2, 2,2,3]
n = len(nums)
print (math.floor(n/2))

def majority_element(nums):
    counts ={}
    n = len(nums)
    for num in nums:
        if num in counts:
            counts[num] +=1            
        else:
            counts[num] =1
    new_dic = dict(sorted(counts.items(),key = lambda item: item[1],reverse=True))

    majority_element = {}
    for key in new_dic: #3:4 ,2:3 #
        if new_dic[key] > math.floor(n/2):            
                majority_element[key] = new_dic[key]
                return key           
        
    return 0
print (majority_element(nums))
    
        
    
   
print(majority_element(nums))
#Duplicate
nums = [10, 30, 10, 20]
def check_if_array_contains_duplicate(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    set1 = set(nums)
    if len(set1) < len(nums):
         return True
    else:
         return False

print(check_if_array_contains_duplicate(nums))

#intersectionm
numbers1 = [1, 2, 2, 6, 7]
numbers2 = [2, 2, 7, 7]
set_num1 =set(numbers1)
set_num2 =set(numbers2)

intersec_array = list(set_num1.intersection(set_num2))
intersec_array.sort(reverse=True)
if len(intersec_array) > 0:
  print(intersec_array.sort())

#Single no

arr = [2, 1, 2, 5, 1]
arr.sort()
print(arr)
global z
global l
z =0 
l = len(arr)
while (z<l and l > 2):
    
    
    if arr[z] == arr[z+1]:
        arr.pop(z)
        arr.pop(z)
        print(arr)
        l = len(arr)
        z = 0
    else:
        z += 1
        l = len(arr)
print(arr)
    
#Square
numbers = [1, 2, 3, 4]
def generate_sorted_array_of_squares(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    list1 = list(map(lambda x:x*x,numbers))
    list1.sort()
    return list1 or []
print(generate_sorted_array_of_squares(numbers))
numbers = [-7, -9, -3, -5]
"""
sum_subset = 0
maximum_sum = 0
    #maximum_sum = sum(numbers)
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        numbers_subset = numbers[i:j+1]
        print (numbers_subset)        
        sum_subset = sum(numbers_subset)
        if maximum_sum == 0 and i == 1:            
            maximum_sum = sum_subset
        elif maximum_sum < sum_subset:
             maximum_sum = sum_subset

"""
max_sum = float('-inf')
sum = 0
    
for num in numbers:
    sum = max(num, sum+num)
    max_sum = max(max_sum, sum)

print(max_sum)

# vote

votes= ["sam", "john", "jamie", "sam","john","jamie"]
dic_vote ={}
for candi in votes:
    if candi in dic_vote:
        dic_vote[candi] += 1
    else:
        dic_vote[candi] = 1
dic_vote_new = dict(sorted(dic_vote.items(),key = lambda item: item[1],reverse=True))
print(dic_vote)
print(dic_vote_new)
total_vote = len(votes)
winner_vote = 0
for value in dic_vote_new.values():
    if value <= total_vote and value > winner_vote:
        winner_vote = value 

winner = [winner for winner in dic_vote_new if dic_vote_new[winner] == winner_vote]
winner.sort()
print(winner[0])
    