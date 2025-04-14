def add_two_variable (a,b):
    sum = a+b # local variable
    a = 3 # local variable
    b = 4 # local variable
    print ("inside function a =",a ,"b =",b)
    return sum
def add_two_variable_global (c,d):
    sum = c+d # local variable
    global a 
    a = 7 # local variable
    global b 
    b = 8 # local variable
    print ("inside function a =",a ,"b =",b)
    return sum
a = 1
b = 2
print ("Outside function a =",a ,"b =",b)
print ("Sum of a = ", a ," & b = " , b , " is : ",add_two_variable(a,b))
print ("a & b after changing values of a,b inside function is :",a,b)
c = a
d = b
print ("Outside function a =",a ,"b =",b)
print ("Sum of c= ",c,"& d = ",d ,"is :",add_two_variable_global(c,d))
print ("a & b after changing values of global variable a,b inside function is :",a,b)
import numpy 
