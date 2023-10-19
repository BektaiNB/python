#RATIO TASK1
def task1():
    num = input("sandar:")
    if len(num) != 4 or not num.digits():
            print("incorrect")
    else:
            birinshi_san = int(num[0])
            ekinshi_san = int(num[1])
            usinshi_san = int(num[2])
            tortinshi_san = int(num[4]) 
            if birinshi_san + tortinshi_san == ekinshi_san - usinshi_san:
                    print("YESS")
            else:
                    print("ZHOKK")

#Roskomnadzor
def task2():
       num = int(input("age:"))
       if num >= 18:
              print("accepted")
       else:
              print("rejected")

#Arithmetic progression
def task3():
        a, b, c = int(input()), int(input()), int(input())
        print('YES' if (c - b) == (b - a) and (a <= b <= c or a > b > c) else 'NO')

#Rook Move
def task4():
        a=int(input())
        b=int(input())
        c=int(input())
        d=int(input())
        if a==c or a==d or b==c or b==d:
            print ('YES')
        else:
            print ('NO')

#King's Move🌶 ️
def task5():
       a, c = int(input()), int(input())
       b, d = int(input()), int(input())
       if (-1 <= a - c <= 1) and (-1 <= b- d <= 1):
              print("Yes")
       else:
              print("NO")
    
#Average number
def task6():
    a = int(input())
    b = int(input())
    c = int(input())
    max_number = max(a, b, c)
    min_number = min(a, b, c)
    middle_number = a + b + c - max_number - min_number
    print(middle_number)

#Number of days
def task7():
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = int(input("Enter the month number: "))
    if 1 <= month <= 12:
        print(f"Number of days in the month: {days_in_month[month]}")
    else:
        print("Invalid month number. Enter a number between 1 and 12.")

#Weigh-in ceremony
def task8():
    m = int(input())
    if m<=59:
        print('Легкий вес')
    elif m>=60 and m<=63:
        print('Первый полусредний вес')
    elif m>=64 and m<=68:
        print('Полусредний вес')

#Password 
def task9():
    password = input()
    password2 = input()
    while len(password) < 8:
        print("Короткий!")
        password = input()
        password2 = input()
    while "123" in password:
        print("Простой!")
        password = input()
        password2 = input()
    while password2 != password:
        print("Различаются.")
        password = input()
        password2 = input()
    else:
        print("OK")

#Even or odd
def task10():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")

#The smallest of two number
def task11():
     num_n = int(input(":"))
     num_m = int(input(":"))
     mini = min(num_n, num_m)
     print(mini)

#Age Group
def task12():
    age=int(input())
    if age>0 and age<=13:
        print( "Childhood")
    elif age>=14 and age<=24 :
        print ( "Youth")
    elif age>=25 and age<=59:
        print( "Maturity")
    elif age>=60:
         print("Old age")
    else:
         print("error")
