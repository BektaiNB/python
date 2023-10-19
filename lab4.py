def num1():
    user_input = input("Enter a string or number: ")
    turtles = tuple(user_input)

    print(turtles)

# num1()



def num2():
    matters = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

    string = ''.join(matters)

    print(string)

# Usage:
# num2()



def num3():
    a = (1, 2, 3, 4, 5, 6, 7)
    c = (5, 6, 7, 9, 7, 1, 10, 10)

    index = len(c) // 2

    b = a[:index] + c[index:]

    print(b)

# num3()



def num4():
    a = input("Numbers: ").split(', ')
    funn = [(i, a.count(i)) for i in set(a)]

    b = tuple(funn)

    print(b)

# num4()


def num5():
    caesar = []

    funny = input("Numbers or strings: ").split(", ")
    caesar.extend(funny)

    strings = [x for x in caesar if not x.replace('.', '', 1).isdigit()]
    integers = [int(x) for x in caesar if x.isdigit()]
    floats = [float(x) for x in caesar if x.replace('.', '', 1).isdigit()]

    print(f"Strings: {strings}\nIntegers: {integers}\nFloats: {floats}")

# num5()

def num2_1():
    user_input = input("Object: ")
    sets = {str(x) for x in user_input}
    print(sets)


# num2_1()

def num2_2():
    inp_a = input("Set a:").split(",")
    inp_b = input("Set b:").split(",")

    set_a = {int(x) for x in inp_a}
    set_b = {int(x) for x in inp_b}

    set_c = set_a ^ set_b

    print(set_c)


# num2_2()

def num2_3():
    inp_a = input("Set a:").split(",")
    inp_b = input("Set b:").split(",")

    set_a = {int(x) for x in inp_a}
    set_b = {int(x) for x in inp_b}

    set_c = set_b - set_a

    print(set_c)


# num2_3()

def num2_4():
    inp_a = set(input("Set a:").split(", "))
    inp_b = set(input("Set b:").split(", "))
    inp_c = set(input("Set c:").split(", "))

    set_a = set(inp_a)
    set_b = set(inp_b)
    set_c = set(inp_c)

    set_a.update(set_c.intersection(set_a))
    set_c.update(set_b.intersection(set_c))

    print("Updated set_a:", set_a)
    print("Updated set_b:", set_b)
    print("Updated set_c:", set_c)

# num2_4()


def num2_5():
    import random

    l_size = int(input("Size: "))
    input_quality = int(input("Quantity: "))

    set_a = {1, 2, 3, 4, 5, 6}
    set_a_copy = list(set_a)
    lists = []

    while len(lists) < l_size:
        funn = []
        while len(funn) < input_quality + 1:
            x = random.choice(set_a_copy)
            if x not in funn:
                funn.append(x)
        if funn not in lists:
            lists.append(funn)

    for i in enumerate(lists, 1):
        print(i)


# num2_5()


def numb3():
    # (‘BMW’, ‘X6’), (‘Toyota’, ‘Yaris’), (‘Fiat’, ‘500’), (‘Fiat’, ‘Panda’), (‘Toyota’, ‘Camry 30’)
    user_input = input("Input: ").replace("‘", "'").replace("’", "'")

    tuples = eval(user_input)
    caesar = list(tuples)
    funn = []

    for brand, name in caesar:
        found = False
        for i in range(0, len(funn), 3):
            if funn[i] == brand:
                funn[i + 1] += 1
                found = True
                if name not in funn[i + 2]:
                    funn[i + 2].append(name)
                break
        if not found:
            funn.extend([brand, 1, [name]])

    print(funn)


# numb3()

