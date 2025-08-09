# identity operators
a=5
if (type(a) is int):
    print("true")
else:
    print("false")
     
a=5.0
if (type(a)is not float):
    print("true")
else:
    print("false")

x=20
y=20
if (x is y):
   print("x and y same identity")
y=30
if (x is not y):
    print("x and y is not same identity") 