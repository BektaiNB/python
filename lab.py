
def task1():
    numbers = [4, 8, 15, 16, 23, 42]
    print(numbers [0], numbers[1],numbers[2], numbers [3], numbers[4], numbers[5])

def task2():
    numbers = [4, 8, 15, 16, 23, 42]
    for i in numbers:
        print(i)

def task3():
    default_numbers = [9, 10]
    output_numbers = []
    try:
        user_input = int(input("Enter your number: "))
        
        output_numbers.append(user_input)
        output_numbers += default_numbers

        for number in output_numbers:
            print(number)

    except ValueError:
        for number in default_numbers:
            print(number)
def task4():

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

    total = first_number + second_number + third_number


    print(total)

def task5():

    num1 = int(input(": "))
    
    overall = num1*num1*num1
    overall2 = 6*(num1*num1)
    print(overall)
    print(overall2)

def task6():
    
    N = int(input("Enter the number of schoolchildren: "))
    K = int(input("Enter the number of tangerines: "))

    if K >= N:
        
        whole_tangerines_per_student = K // N
        
        remaining_tangerines = K % N
        
        print(whole_tangerines_per_student)
        print(remaining_tangerines)
    else:
        print("The number of tangerines is less than the number of schoolchildren, so each student cannot get any tangerines.")

def task7():
    number = int(input("number: "))

    if 1000 <= number <= 9999:
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        print("Thousands:", thousands)
        print("Hundreds:", hundreds)
        print("Tens:", tens)
        print("Ones:", ones)
    else:
        print("The number is not a four-digit number.")

def task8():
    import math
    population = int(input("Enter the population of the universe: "))

    if population <= 0:
        print("Invalid population. Please enter a positive number.")
    else:
        if population % 2 == 0:
            survivors = population // 2
        else:
            survivors = math.ceil(population / 2)
        print("Number of survivors:", survivors)
def task9():
    population = int(input("number:"))
    result = population << 1
    if result == 0:
        print("<< is zero")
    else:
        print(f"The result of << is {result}")

def task10():
    try:
        f_num = float(input("Please enter the first number: "))
        s_num = float(input("Please enter the second number: "))
        operation = input("Please choose the operation (+, -, *, /): ")

        if operation == '+':
            result = f_num + s_num
        elif operation == '-':
            result = f_num - s_num
        elif operation == '*':
            result = f_num * s_num
        elif operation == '/':
            if s_num == 0:
                print("Division by zero is not allowed.")
                result = None
            else:
                result = f_num / s_num
        else:
            print("Invalid operation. Please choose from +, -, *, /")

        if result is not None:
            print(f"{f_num} {operation} {s_num} = {result:.3f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

