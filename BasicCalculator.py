def sum(num_one, num_two):
    return num_one + num_two

def extract(num_one, num_two):
    if num_one >= num_two:
        return num_one - num_two
    else:
        return num_two - num-one

def divide(num_one, num_two):
    if num_one >= num_two:
        return num_one / num_two
    else:
        return num_two / num - one

def multiply(num_one, num_two):
    return num_one * num_two

num_one = float(input("Enter your first number: "))
operator = input("Enter operator:")
num_two = float(input("Enter your second number: "))

if operator == "*":
    print(multiply(num_one, num_two))
elif operator == "/":
    print(divide(num_one, num_two))
elif operator == "+":
    print(sum(num_one, num_two))
elif operator == "-":
    print(extract(num_one,num_two))
else:
    print("Please enter correct operator!")


