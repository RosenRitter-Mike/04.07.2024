num1: int = int(input("first number: "));
num2: int = int(input("second number: "));
if num1 > num2:
    print(num1, "is the larger number");
elif num2 > num1:
    print(num2, "is the larger number");
else:
    print("the numbers are equal");