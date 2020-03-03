def fib(n):
    a = [0, 1]
    lastnum = None
    if n == 0:
        lastnum = a[0]
    elif n == 1:
        lastnum = a[1]
    else:
        for n in range(1, n):
            lastnum = a[-1] + a[-2]
            a.append(lastnum)
    return lastnum


def main():
    # FIBONACCI
    i = 0
    while True:
        fib_num = fib(i)
        print("Result from Fibonacci iteration " + str(i) + ": " + str(fib_num))
        i += 1


if __name__ == '__main__':
    main()
