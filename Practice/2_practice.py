# írj egy függvényt, ami kiírja a számokat 1-10-ig
# írj egy függvényt, ami visszaad egy listát, benne a számokkal 1-10-ig
# írj egy függvényt, ami visszaadja a paraméternek megadott szám faktoriálisát
# írj egy függvényt, ami visszaadja a paraméternek megadott másodfokú egyenlet megoldásait
# írj egy függvényt, ami kiírja a paraméternek megadott szám abszolút értékét
# írj egy függvényt, ami elszámol 100-ig úgy, hogy minden 3-mal osztható szám helyett az írja ki hogy Fizz
    # minden 5-tel osztható számra azt írja ki hogy Buzz, és ami mindkettővel osztható, arra azt hogy FizzBuzz 
import math

def numbers_one_to_ten():
    for i in range(1,11):
        print(i)


def list_one_to_ten():
    my_list=[]
    for i in range(1,11):
        my_list.append(i)
    return my_list

def factorial(n):
    tmp=1
    for i in range(1,n+1):
        tmp = tmp*i
    return tmp
    

def quadratic(a, b, c):
    d = b*b-4*a*c
    if d < 0:
        print("fasz")
    else:
        if d == 0:
            print(-b/2*a)
        else:
            print((-b+math.sqrt(d))/(2*a))
            print((-b-math.sqrt(d))/(2*a))

def abs(n):
    if n > 0:
        return n
    else:
        return n * (-1)

def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        else:
            if i % 3 == 0:
                print("Fizz")
            else:
                if i % 5 ==0:
                    print("Buzz")
                else:
                    print(i)


def create_dict():
    keys = ['a', 'b', 'c', 'd']
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = i + 1
    return my_dict

def print_dict(my_dict):
    for key, value in my_dict.items():
        print(key, value)


if __name__ == '__main__':
    numbers_one_to_ten()
    q = list_one_to_ten()
    print(q)

    f = factorial(5)
    print(f)

    print(factorial(5))

    print(abs(-4))
    print(abs(6))
    print(abs(0))
    print()
    fizz_buzz()
    print()
    quadratic(2, 16, 9)

    my_dict = create_dict()
    print_dict(my_dict)

