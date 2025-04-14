numbers = [1,2,3,4,5]
def reverse_an_array(numbers):
    start,end = 0, len(numbers)-1
    while (start < end):
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1
    
    return numbers

print (reverse_an_array(numbers))
