print("===Simple calculator===")
numa = float(input("Enter first number:"))
operator=input("Enter the operation(+,-,*,/):")
numb=float(input("Enter second no:"))

if operator=="+":
    print(numa+numb)
elif operator=="-":
    print(numa-numb)
elif operator=="*":
    print(numa*numb)
elif operator=="/":
    if numb !=0:
        result = numa/numb
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"
print(result)