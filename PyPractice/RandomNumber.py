import random
n=999999
obj=open("D:/sparkecosystem/data/RandomOTP.txt","w")
while True:
    a=random.randrange(100000,999999)
    obj.write(str(a))
    obj.write("\n")
    n=n-1
obj.close()
