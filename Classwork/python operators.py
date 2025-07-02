#Arithmetic operators
a=10
b=20
print("Addition(+):",a+b)
print("subtraction(-):",a-b)
print("Multiplication(*):",a*b)
print("division(/):",a/b)
print("floor division(//):",a//b)
print("Modulus(%):",a%b)
print("Exponential(**):",a**b)

#Comparision operators
a=5
b=10
print("Equal to(==):",a==b)
print("Not Equal to(!=):",a!=b)
print("Greater than(>):",a>b)
print("Less than(<):",a<b)
print("Greater than or equal to(>=):",a>=b)
print("Lesser than or equal to(<=):",a<=b)

#Assignment operator
a=10
print("Assign(=):",a)
a=a+5
print("Add & Assign(+=):",a)
a=a-5
print("Subtract & Assign(-=):",a)
a=a*2
print("Multiply & Assign(*=):",a)
a=a/5
print("division & Assign(/=):",a)
a=a//1
print("Floor division & Assign(//=):",a)
a=a**5
print("Exponential & Assign(**=):",a)

#Logical operator
a=6
b=10
print("And:",a>b and b>a and a<b)
print("And:",a%3==0 and b%5==0)
print("Or:",a%2==0 or b%3==0)
print("Not:",not b%3==0)

#Membership operators
#list
L=["Mounika","Sreeja","Harika","Bhavana","Hema"]
print("Mounika" in L)
print("mounika" in L)
print("Lekha" in L)
print("Bhavana" in L)
#Tuple
t=(1,2,3,4)
print(1 in t)
print(5 in t)
print(3 not in t)
print(4 in t)
#Set
s=(1,5,8,3)
print(1 in s)
print(5 not in s)
print(4 in s)
print(8 in s)
#Dictionary
d={'Name':"Harika",'Course':"DS",'age':"21"}
print('Name' in d)
print("21" in d)
print('Course' in d)
print('age' in d)

#Identity operators
a=[1,2,3,4]
b=[1,2,3,4]
c=[3,4,5,6]
a=b
print(a is b)
print(a is not c)
print(b is c)
print(a is c)


