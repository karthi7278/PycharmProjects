import string
from random import *
n=999999
obj=open("D:/sparkecosystem/data/RandomPasswords.txt","w")
while True:
    characters=string.ascii_letters+string.punctuation+string.digits
    password= "".join(choice(characters) for x in range(randint(8,16)))
    n = n - 1
    obj.write(str(password))
    obj.write("\n")

obj.close()
