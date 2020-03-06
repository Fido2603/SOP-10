def fib(n):
    # Create array with the first two instances of the Fibonacci sequence
    # We use this array to slowly add the values we figure out, so that we only have to look two values behind
    a = [0, 1]
    if n == 0:
        return a[0]  # If the number entered is 0, return first index of array (0)
    elif n == 1:
        return a[1]  # If the number entered is 1, return the second index of array (1)
    else:
        for n in range(1, n):  # Does the following for every number from 1 to n
            a.append(a[-1] + a[-2])  # Add the newest index in the array to the second newest index to the array
        return a[-1]  # Return newest index in the array


def fib_noarray(n):
    if n == 0:
        return 0  # If the number entered is 0, return first index of array (0)
    elif n == 1:
        return 1  # If the number entered is 1, return the second index of array (1)
    else:
        first = 0
        second = 1

        lastnum = None  # Variable used for the final number found
        for n in range(1, n):  # Does the following for every number from 1 to n
            lastnum = first + second
            first = second
            second = lastnum

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
