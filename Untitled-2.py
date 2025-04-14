
a = [7, 7, 14, 92, 14, 92, 92]
b = [0, 0, 92, 92, 7]

dic1 = {}
dic2 = {}
for i in a:
    if i in dic1:
        dic1[i] +=1
    else:
        dic1[i] = 1
for i in b:
    if i in dic2:
        dic2[i] +=1
    else:
        dic2[i] = 1

new_list =[]
print (dic1,dic2)
for key1 in (dic1):
    if key1 in (dic2):                 
            min_val = min(dic1.get(key1),dic2.get(key1))
            new_list.extend([key1]*min_val)
            
            
print(new_list)
print(new_list1)
