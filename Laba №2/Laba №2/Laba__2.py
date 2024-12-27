# 1)
def greet(na):
    return('Приветствую, ' + na)
print(greet('Орлов Никита'))


def square(n):
    return n * n
n=int(input())
print(square(n))


def max_of_two(a, b):
    if a > b:
        return a
    return b
a = int(input('Введите число '))
b = int(input('Введите число '))
print('Максимальное число:', max_of_two(a, b))

# 2)
name = input()
#age = int(input())

def describe_person(name, age=30):
    return f'My name is {name} i am {age}'
print(describe_person(name))

# 3)
ni = int(input())
def is_prime(ni):
    a=0
    for i in range(1,ni):
        if ni % i ==0:
            a += 1
    if a == 1:
        print('true')
    else:
        print('false')
is_prime(ni)

def is_prime(ni):
    if ni <= 1:
        return False
    if ni == 2:
        return True
    if ni % 2 == 0:
        return False
    for i in range(3, int(ni ** 0.5) + 1, 2):
        if ni % i == 0:
            return False
        return True
    
def is_prime(ni):
    if ni <= 1:
        return False
    for i in range(2, int(ni**0.5) + 1):
        if ni % i == 0:
            return False
        return True