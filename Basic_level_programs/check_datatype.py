#Store an HTTP status code (e.g. 200) in a variable and confirm it's an `int` with `type()`.

n=200
#simple program to check data type
if type(n) is int:
    print(f"{n} is of type int")

#complex program to check data for each type
datatype=["int","float","complex","str","bool","list","tuple","set","dict"]
for i in datatype:
    if isinstance(n, eval(i)):
        print(f"{n} is of type {i}")
