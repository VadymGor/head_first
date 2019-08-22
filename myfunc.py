def myfunc(*args):
    for a in args:
        print(a, end=' ')
        if args:
            print()


values = [1, 2, 3, 4, 5, 7, 11]

myfunc(values)

myfunc(*values)
