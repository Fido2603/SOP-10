def fib(n):
    # If the input number is 0, return 0
    if n == 0:
        return 0
    # If the input number is 1, return 1
    elif n == 1:
        return 1
    else:
        # Recursiveness, call back to itself, to find the fibonacci value below and the fibonacci value two steps below
        return fib(n - 1) + fib(n - 2)


def main():
    # FIBONACCI
    i = 0
    while True:
        fib_num = fib(i)
        print("Result from Fibonacci iteration " + str(i) + ": " + str(fib_num))
        i += 1


if __name__ == '__main__':
    main()
