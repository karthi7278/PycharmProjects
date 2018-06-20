a={'a':15,'b':20}
print(a['a'])

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
print(Boys)
print(Girls)
x=Boys.copy()
y=Girls.copy()

print(x)
print(y)

Dict.update({"Robert":30})
print(Dict)

del Dict['Charlie']
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 20,'Charlie':21,'Robert':22}
Girls = {'Tiffany':22}

for key in list(Boys.keys()):
    for key in list(Dict.keys()):
        print(True)
    else:print(False)

    Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
    Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
    Girls = {'Tiffany': 22}
    Students = list(Dict.keys())
    Students.sort()
    for S in Students:
        print(":".join((S,str(Dict[S]))));
        #print(":".join((S, str(Dict[S]))))
print("Length: %d" % len(Dict))

print("Variable Type: %s" %type(Dict))