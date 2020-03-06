import datetime
import sys
from Util import SheetManager
import Fibonacci_recursive
import Fibonacci_nonrecursive


def main():
    # Log the Python version
    print("")
    print("---- PYTHON VERSION ----")
    print(sys.version)
    print("------------------------")

    # Testing the different sortings
    iterations = 200  # Running the different sortings this amount of times

    # # Recursive fibonacci #
    # print("---- Fibonacci RECURIVE ----")
    # type = "Fibonacci Recursive"

    # Non-recursive fibonacci #
    print("---- Fibonacci NON-RECURIVE ----")
    type = "Fibonacci Non-recursive"

    # Do testing
    ws = SheetManager.new_worksheet(type + "-" + str(iterations) + "ite")
    number = 0
    while True:
        if number > 4000:
            break
        testSorter(ws, type, number, iterations)
        number += 1


def testSorter(ws, type, number=None, iterations=1000):
    if type is None:
        print("Type is none!")
        return
    if number is None:
        print("Number is none!")
        return

    # Setting up variable for all time taken during the number of iterations
    all_time = 0
    # Setting up variable for minimum value and maximum value
    minimum = None
    maximum = 0

    i = 1
    while i <= iterations:
        if "Fibonacci Recursive" in type:
            output = testFibonacciRecursive(number)
        elif "Fibonacci Non-recursive" in type:
            output = testFibonacciNonRecursive(number)
        else:
            print("No testing type given!!")
        time = output[1]
        # print(str(time))

        # Update minimum and maximum
        if minimum is None:
            minimum = time

        if time < minimum:
            minimum = time
        if time > maximum:
            maximum = time

        # Add time to alltime_variable_name
        all_time = all_time + time
        i += 1

    # Getting the average time, and saving it
    average_time = all_time/iterations

    print("Writing to spreadsheet!")
    if number < 1476:  # At 1476 the Fibonacci number gets too big to convert from int to float in Python, so OpenPyXL breaks
        SheetManager.write_newentry((number, average_time, minimum, maximum, output[0]), ws)
    else:
        SheetManager.write_newentry((number, average_time, minimum, maximum), ws)

    print("Done writing to spreadsheet!")

    print("Time taken, average, for a " + type + " type, with a number of " + str(number) + ", during " + str(
        iterations) + " iterations: " + str(average_time) + " ms [" + str(minimum) + " ms // " + str(maximum) +
        " ms]")
    return average_time


def testFibonacciRecursive(number):
    time_start = datetime.datetime.now()  # Starts the time

    fib = Fibonacci_recursive.fib(number)  # Runs the Function

    time_end = datetime.datetime.now()  # Ends the time

    # Return elapsed time
    elapsed_time = time_end - time_start
    return [fib, elapsed_time.total_seconds() * 1000]


def testFibonacciNonRecursive(number):
    time_start = datetime.datetime.now()  # Starts the time

    fib = Fibonacci_nonrecursive.fib_noarray(number)  # Runs the Function

    time_end = datetime.datetime.now()  # Ends the time

    # Return elapsed time
    elapsed_time = time_end - time_start
    return [fib, elapsed_time.total_seconds() * 1000]


if __name__ == '__main__':
    main()
