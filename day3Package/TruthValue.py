#Truth Value
#Non-empty strings are treated as True.
#Empty strings are treated as False.

name=input("Enter value of name : ")
if name:
    print(f"True as name is : {name}, Datatype is {type(name)}")
else:
    print(f"False as name is : {name}, Datatype is {type(name)}")

