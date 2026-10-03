'''
Range()- is a function.
1. Range(stop)- starts from 0 and stops before the given number.
    e.g. range(5) -> 0,1,2,3,4
2. Range(start,stop,step)
    start- starting value
    stop- ending value/limit
    step- increment/decrement value
    e.g. range(1,10,2) -> 1,3,5,7,9
'''
print("Print numbers from 0 to 9")
Num1=int(input("Enter a number1 : "))
for counter in range(Num1):
    print(counter)

print("Print even numbers from 2 to 20")
Num2=int(input("Enter a number2 : "))
for counter in range(2,Num2,2):
    print(counter)

print("Print odd numbers from 1 to 19")
Num2=int(input("Enter a number2 : "))
for counter in range(1,Num2,2):
    print(counter)


# while loop continues as long as the condition is True.
# It stops when the condition becomes False.

