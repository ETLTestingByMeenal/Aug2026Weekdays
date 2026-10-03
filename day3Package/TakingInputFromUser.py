#INPUT() - Input is used to take data from user.
#By default, input() always returns data as a STRING.

name=input("Enter your name: ")
print(f"Name is : {name}")
print(f"Datatype of {name} is {type(name)}")

#Convert string into integer
age=int(input("Enter your age: "))
print(f"Age is : {age}, converted string into integer")
print(f"Datatype of {age} is {type(age)}")
age_float=float(age)
print(f"Datatype of {age_float} is {type(age_float)}")

height=5.6
print(f"Height is : {height}, Datatype of {height} is {type(height)}");
height_int=int(height)
print(f"Height is : {height_int}, Datatype of {height_int} is {type(height_int)}");

