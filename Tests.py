def product(*factors):
    k = 1
    for x in factors:
        k = k*x
    print(k)

product(2, 3, 4)