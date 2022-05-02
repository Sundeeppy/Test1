def First5Multiples():
    print("6 * 1 =", (6 * 1))
    print("6 * 2 =", (6 * 2))
    print("6 * 3 =", (6 * 3))
    print("6 * 4 =", (6 * 4))
    print("6 * 5 =", (6 * 5))

print("Hello")
b = 3
print("Function First5Multiples() will print", b+2, "multiples of 6.")
First5Multiples()

if b+2 >= 5 :
    print("The Function Printed", b + 2, "multiples of 6.")
    print("Python is amazing !")
    print("I Have started enjoying myself.")

def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(1,2,3, last=100)

def foo(a,b,c):
    print(a,b,c)

my_list = (0,1,2) # to unpack list
foo(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3} # to unpack dictionary
foo(**my_dict)

def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)

number = 0
foo()
print(number)





