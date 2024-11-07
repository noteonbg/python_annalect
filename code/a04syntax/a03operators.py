a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333333333333335
print(a // b)  # Floor Division: 3
print(a % b)   # Modulo: 1
print(a ** b)  # Exponentiation: 1000

x = 5
y = 10

print(x == y)   # False (5 is not equal to 10)
print(x != y)   # True (5 is not equal to 10)
print(x > y)    # False (5 is not greater than 10)
print(x < y)    # True (5 is less than 10)
print(x >= y)   # False (5 is not greater than or equal to 10)
print(x <= y)   # True (5 is less than or equal to 10)

a = True
b = False

print(a and b)   # False (both conditions must be True)
print(a or b)    # True (at least one condition must be True)
print(not a)     # False (inverts the value of a)


x = 5
x += 3   # x = x + 3
print(x)  # 8

x *= 2   # x = x * 2
print(x)  # 16

a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # 0 (Bitwise AND: 1010 & 0100 = 0000)
print(a | b)  # 14 (Bitwise OR: 1010 | 0100 = 1110)
print(a ^ b)  # 14 (Bitwise XOR: 1010 ^ 0100 = 1110)
print(~a)      # -11 (Bitwise NOT: Inverts all bits)
print(a << 1)  # 20 (Left shift: 1010 << 1 = 10100)
print(a >> 1)  # 5 (Right shift: 1010 >> 1 = 0101)


#membership operators
lst = [1, 2, 3, 4, 5]
s = "Hello"

print(3 in lst)      # True (3 is in the list)
print(6 not in lst)  # True (6 is not in the list)
print('e' in s)      # True ('e' is in the string)
print('z' not in s)  # True ('z' is not in the string)

#identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (a and b are different objects, though their values are the same)
print(a is c)      # True (a and c point to the same object)
print(a is not b)  # True (a and b do not refer to the same object)

#ternary operator
x = 10
y = 20

# Ternary operator
max_value = x if x > y else y
print("Max value:", max_value)  # 20

"""
Arithmetic Operators: +, -, *, /, //, %, **
Comparison Operators: ==, !=, >, <, >=, <=
Logical Operators: and, or, not
Assignment Operators: =, +=, -=, *=, /=, etc.
Bitwise Operators: &, |, ^, ~, <<, >>
Membership Operators: in, not in
Identity Operators: is, is not
Ternary Operator: x if condition else y

"""

