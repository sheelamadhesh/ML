#Write a Python program to sort a list of strings based on the length of each string. Define a custom sort function that takes a list of strings and returns a sorted list.

"""
list1 = ["Hi","this","is","sorting","problem"]
def sorted_list_of_string (list1):
    # get a list
    # create a dic_sort with element as key and length of string as value
    # Sort dic_sort based on count. i.e : value of dic 
    # convert dic_sort as list and return
    dic_sort = {}
    for element in list1:
        dic_sort[element] = len(element)
    
    dic_sorted = list(dict(sorted(dic_sort.items(),key = lambda item: (item[1],item[0]),reverse=False)))
    return dic_sorted               
     

print(sorted_list_of_string (list1))


def sort_strings_by_length(list1):
  return sorted(list1, key= len)

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_list = sort_strings_by_length(my_list)
print(sorted_list) # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']
print(sorted_list_of_string (my_list))


#Exception
# How can you ensure that a certain code block runs no matter whether there’s an exception or not?

# We can write the code block inside finally block
a = 4
b = 0
try:
   division = a/b
except ZeroDivisionError: # Handling of exception (if required)
   print("dividing by zero error") 
else: # execute if no exception
   print ("answer is : ",division)
finally: #(always executed)
   print ("i'm always executed")


What do you understand about the traceback module in Python?
The traceback module in Python provides methods for working with and printing stack traces. A stack trace is a report that shows 
the sequence of function calls leading up to an error or exception in your program.
When an exception occurs, Python automatically generates a traceback that includes information about the line number, file name, 
and function calls that led to the exception. The traceback module provides functions to customize, format, and print this traceback information.
Using the traceback module, you can programmatically access the traceback information and extract details about the error, such as the 
specific line of code where the exception occurred or the function calls that led to the error. This can be useful for debugging 
and understanding the flow of your program.
Some of the commonly used functions in the traceback module include traceback.format_exc() for formatting the traceback as a string, 
traceback.print_tb() for printing the traceback to the console, and traceback.extract_tb() for extracting individual frames from the traceback.
Overall, the traceback module is a powerful tool for diagnosing and troubleshooting errors in Python programs by providing 
valuable information about the sequence of function calls leading up to the error.
"""
#Write a Python program to find the longest word in a file.


#Write a Python program that reads data from a JSON file and prints the contents of the file to the console.
#Open file from local
#read file content and assign it to string variable
#replace \n(new line space) with " "
#create new list using split function
#sort the list in decending order.Key is length of each word
#print longest word

file_obj = open(r"D:\Sheela\Net\file_open.txt","r")
string_list = file_obj.read().split()
#string = string.replace("\n"," ")
#string_list = string.split(" ")
sorted_list = sorted(string_list,key=len,reverse=True)
print(sorted_list[0])

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('file_open.txt'))

#Write a Python program that prompts the user for two numbers and divides them. Handle any exceptions that may arise from the division.

print ("please input number1")
string1 = input()
print("Please input number2")
string2 = input()
number1 = int(string1)
number2 = int(string2)
try:
    result = number1 / number2
except ZeroDivisionError:
    print("zero divide by error")
else:
    print("result is:",result)
finally:
    print("program executed finally")

    #Write a Python program that reads data from a JSON file and prints the contents of the file to the console.

    import json
    jason_obj = open("test.json")
    dic_json = json.load(jason_obj)
    print (dic_json)