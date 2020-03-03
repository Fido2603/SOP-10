look = [1, 1]
say = []

while True:
    currentval = None
    times = 1
    for val in look:
        if currentval is None:
            currentval = val
        elif currentval == val:
            times += 1
        else:
            say.append(times)
            say.append(currentval)

            times = 1
            currentval = val

    print(say)
    look = say
    say = []
