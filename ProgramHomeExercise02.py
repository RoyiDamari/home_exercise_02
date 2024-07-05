# Exercise 1
# The long code
x: int = int(input("Please enter an integer: "));
y: int = int(input("Please enter one more integer: "));
z: int = int(input("Please enter one more integer: "));
print("sum: ", x + y + z);
print("multiplication: ", x * y * z);

# The Short code
x, y, z = map(int, input("Please enter 3 integers separated by spaces: ").split());
print("sum: ", x + y + z);
print("multiplication: ", x * y * z);

# Exercise 2
# The long code
x: float = float(input("Please enter a decimal number: "));
y: float = float(input("Please enter one more decimal number: "));
z: float = float(input("Please enter one more decimal number: "));
print("subtraction: ", x - y - z);

# The Short code
x, y, z = map(float, input("Please enter 3 decimal numbers separated by spaces: ").split());
print("subtraction: ", x - y - z);

# Exercise 3
str1, str2 = map(str, input("Please enter 2 strings separated by spaces: ").split());
print("*" + str1 + "*" + str2 + "*");
print("-" + str1 + "-" + str2 + "-");

# Exercise 4
num1, num2 = map(int, input("Please enter 2 integers separated by spaces: ").split());
if num1 > num2:
    print(num1);
else:
    print(num2);

# Exercise 5
num1, num2 = map(int, input("Please enter 2 integers separated by spaces: ").split());
if num1 >= num2:
    print(num2);
    print(num1);
else:
    print(num1);
    print(num2);