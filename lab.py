
def task1():
    numbers = [4, 8, 15, 16, 23, 42]
    print(numbers [0], numbers[1],numbers[2], numbers [3], numbers[4], numbers[5])
 
def task2():
    numbers = [4, 8, 15, 16, 23, 42]
    for i in numbers:
        print(i)
    
def task3():
    num_rows = int(input("San zhaz: "))


    for i in range(1, num_rows + 1):
        print("*" * i)
#basqa
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
        
        print(f"Each student will get {whole_tangerines_per_student} whole tangerines.")
        print(f"There will be {remaining_tangerines} whole tangerines remaining in the basket.")
    else:
        print("The number of tangerines is less than the number of schoolchildren, so each student cannot get any tangerines.")

def task7():
    number = int(input("Enter a four-digit number: "))

    if 1000 <= number <= 9999:
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        print("Thousands digit:", thousands)
        print("Hundreds digit:", hundreds)
        print("Tens digit:", tens)
        print("Ones digit:", ones)
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

