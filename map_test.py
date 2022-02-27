def f(x):
    return x * x


if __name__ == '__main__':
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    list(r)
    print(r,list(r))

