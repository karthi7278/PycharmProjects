tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);

print(tup1[0])
print(tup2[1:4])

x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)

a=(5,6)
b=(1,4)

if(a>b):print("a is bigger")
else:print("b is bigger")

c=(5,6)
d=(5,4)
if (c>d):print("c is bigger")
else: print ("d is bigger")

e=(5,6)
f=(6,4)
if (e>f):print("e is bigger")
else: print("f is bigger")

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print (b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print (x[2:4])
