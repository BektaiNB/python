#task1
def task1():
    name = str(input("Enter your name please:"))
    salary = int(input("Enter your desired salary level:"))
    if salary == int:
        print(name, ("Enter your desired salary level:"), salary, "is:",  salary * 2)
    else:
        print(name, "please enter your desired salary as a digit")

#task2
def task2():
    operations = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        3: lambda x, y: x / y,
        4: lambda x, y: x ** y
    }

    print("Please choose the task you want to perform:")
    print("1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation")

    task = int(input("User Input: "))

    if task in operations:
        print("Please enter two numbers for the operation, comma separated")
        numbers = input("User Input: ").split(',')
        num1, num2 = map(float, numbers)
        result = operations[task](num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice.")

#task3
def task3():
    operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
    4: lambda x, y: x ** y
}

print("Please chose the task you want to perform:")
print("1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation")
task = int(input("User Input:\n"))

if task in operations:
    print("Please enter two numbers for the operation, comma separated")
    numbers = input("User Input:\n").split(',')
    num1, num2 = map(float, numbers)
    result = operations[task](num1, num2)
    print(result)
else:
    print("Invalid choice.")

#task4
def task4():
    unique_items = set()
    non_unique_items = {}

while True:
    print("Please choose the task you want to perform:")
    print("1. Enter items\n2. Exit")
    choice = input("User Input: ")

    if choice == '1':
        items_input = input("Please enter items separated by a comma: ")
        items = [item.strip() for item in items_input.split(',')]
        
        for item in items:
            if item in unique_items:
                non_unique_items[item] = non_unique_items.get(item, 0) + 1
            else:
                unique_items.add(item)
        
        print("Items are saved")
        print("Unique items:", unique_items)
        print("Non-unique items:", [(key, value) for key, value in non_unique_items.items()])
    elif choice == '2':
        break
    else:
        print("Invalid choice.")
