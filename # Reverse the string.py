# Reverse the string 1
a = [1,2,3,4,5]
print (len(a))
b=[]
for i in range(-1,-(len(a)+1),-1):
    b.append(a[i])
print (b) 
# Reverse the string 2
a = [1,2,3,4,5]
start = 0
end = len(a) - 1
print (start,end)
while start < end:
    a[start],a[end] = a[end],a[start]
    start +=1
    end -=1
print (a)
# Reverse the string 3
a.reverse
print (a)