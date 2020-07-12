import sys

try:
    x =int(input("x:")) 
    y =int(input("y:"))
except ValueError:
    print("Error: Invalid input!! please enter numeric value")
    sys.exit(1)



try:
    div = x/y
except ZeroDivisionError:
    print("Error: Divide by zero not possible")
    sys.exit(1)

print(f"{x}/{y} = {div}")