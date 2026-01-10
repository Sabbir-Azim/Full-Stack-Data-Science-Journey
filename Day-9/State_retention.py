def running_average():
    total = 0
    count = 0
    average = None

    while True:
        new_value = yield average

        total += new_value
        count += 1
        average = total/count

ra = running_average()
next(ra)
print(ra.send(5))
print(ra.send(10))
print(ra.send(20))