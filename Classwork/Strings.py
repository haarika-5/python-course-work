#String
Name="Harika"
print(type(Name))

#1.String Operations
#Concatenation
fname='Eluru'
lname='Harika'
print(fname+lname)

#Repetition
name="Pavan"
print("Pavan"*5)

#Indexing
text="Pavankumar"
print(text[3])
print(text[0])
print(text[-5])
print(text[-5])

#Slicing
name="Srilekha"
print(name[0:5])
print(name[:8])
print(name[3:])
print(name[:])

#Membership
name="Harika"
print('Hari' in name)
print('Hari' not in name)
print('kumar' in name)
print('kumar' not in name)

#2.String Functions
#len()
name="Harika"
print(len(name))

#max() and min()
name="pavanXYZ"
print(max("chinnuXYZ"))
print(min("chinnuXYZ"))

#Sorted()
name="chinnu"
print(sorted("chinnu"))

#chr() and ord()
X=('A')
print(ord(X))
X=('a')
print(ord(X))
X=('@')
print(ord(X))
#chr()
print(chr(97))
print(chr(45))
print(chr(81))

#3.String Case Conversion Methods
#Uppercase()
name="Harika"
print(name.upper())
#Lowercase
name="Pavan"
print(name.lower())
#capitalize()
name="srilekha"
print(name.capitalize())
#title()
name="string methods"
print(name.title())
#swapcase()
name="aBcDeFgHiJ"
print(name.swapcase())
#casefold()
name= 's'
print(name.casefold())

#4.Alignment & Formating Method
#center()
name='Harika'
print(name.center(20,'*'))
name="Pavan"
print(name.center(30,"-"))
#ljust()
name="lekha"
print(name.ljust(10,"^"))
#rjust
name="strings"
print(name.rjust(20,"-"))
#Zfill
a="741"
print(a.zfill(6))

#5.search & Find Methods
#find()
name="pavan"
print(name.find("a"))
name="lekha"
print(name.find("l"))
#rfind()
name="abcdabcdabcd"
print(name.rfind("d"))
#index
name="python"
print(name.index("t"))
print(name.index("o"))
#rindex()
name="abcabcabcabc"
print(name.rindex("c"))
print(name.rindex("a"))
#count()
name="pythoncourse"
print(name.count("o"))

#6.String Testing Methods
#startswith()
name="21G21A0205"
print(name.startswith("21"))
name="DS15"
print(name.startswith("DS"))
name="ABC123"
print(name.startswith("123"))
#endswith()
name="pavan"
print(name.endswith("an"))
name="lekha"
print(name.endswith("lek"))
#isalpha()
name="Hello"
print(name.isalpha())
name="ABC123"
print(name.isalpha())
#isalnum()
name="abc"
print(name.isalnum())
name="abc123"
print(name.isalnum())
name="@123"
print(name.isalnum())
#islower()
name="Harika"
print(name.islower())
name="PAVAN"
print(name.islower())
#isupper()
name="YOUR FAV COLOUR"
print(name.isupper())
name="your fav colour"
print(name.isupper())
#isspace()
name="    "
print(name.isspace())
#istitle()
name="print hello"
print(name.istitle())
name="Print Hello"
print(name.istitle())
#isidentifier()
name="python1"
print(name.isidentifier())
name="@python"
print(name.isidentifier())

#7.Replace & Modify Methods
#replace()
name="pastan"
print(name.replace("st","v"))
#translate()
name="abc"
print(name.translate(str.maketrans("a","x")))
#maketrans()
name="python"
print(name.maketrans("th","#$"))

#8.splitting & joining Methods
#split()
name="x,y,z"
print(name.split(","))
#rsplit()
name='u,v,x,y,z'
print(name.rsplit(",",1))
#splitlines()
name="Harika\nEluru"
print(name.splitlines())
#join()
name="pavan kumar"
print(",".join(name))
#partition()
name="python-course"
print(name.partition("-"))
#rpartition()
name="python-course"
print(name.rpartition("-"))
print(name.rpartition("-"))

#9.whitespace & Trimming Methods
#strip()
name= " Lekha "
print(name.strip())
#lstrip()
name="----lekha"
print(name.lstrip("-"))
#rstrip()
name="lekha-----"
print(name.rstrip())

#10. & Decoding Methods
#encode()
name="pavan"
print(name.encode())

#decode()
name=b'pavan'
print(name.decode())
