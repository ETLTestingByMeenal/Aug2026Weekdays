'''
Looping Statement- Loops are used to execute a block of code repeatedly.
Python mainly provides:
1. for loop - Iterates over a sequence (list, tuple, string, range) and
    executes block of code for each time.
2. while loop - Repeats a block of code as long as the condition is true.
'''

print("For loop- Iterates over a sequence (list, tuple, string, range) and executes block of code for each time")
for i in range(5): #Iterates over numbers from 0 to 4
    print(i)

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

print("**********************************************************************")

# while loop continues as long as the condition is True.
# It stops when the condition becomes False.
print("While loop- Repeats block of code as long as condition is true")
i=0
while i<5:
    print(i)
    i+=1

print("Print numbers from 1 to 10")
start_val=1
end_val=10
while start_val<=end_val:
    print(start_val)
    start_val = start_val + 1
# Increase the value to eventually make condition False
# start_val=start_val+1
print("**********************************************************************")




