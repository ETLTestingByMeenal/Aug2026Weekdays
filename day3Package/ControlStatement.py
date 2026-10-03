#Control Statement-Control statement controls the flow of an execution.
# 1. if - executes a block of code if the condition is true.
# 2. else - executes a block of code if the condition is true.
# 3. elif (elseif) - Checks multiple conditions and executes block of code
# for the first true condition.

print("1. if statement")
x=2
if x>5:
    print(f"{x} is greater than 5")
age=19
if age>=18:
    print(f"{age} is greater than or equal to 18, eligible for voting")
print("****************************************************************")


print("2. if..else statement")
x=2
if x>5:
    print("x is greater than 5")
else:
    print("x is less than 5")

age=19
if age>=18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
print("****************************************************************")

print("3. if..elif..else (if..elseif..else) statement")
x=21
if x<5:
    print("x is lesser than 5")
elif x==10:
    print("x is 10")
else:
    print("x is greater than 5 however not 10")

age=int(input("Enter age of the person : "))
if age>18:
    print(f"Eligible for voting as age is : {age}")
elif age==18:
    print(f"Near eligible for voting as age is : {age}")
else:
    print(f"Not eligible for voting as age is : {age}")
print("****************************************************************")

