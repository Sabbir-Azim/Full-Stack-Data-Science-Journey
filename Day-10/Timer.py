import time

def timer(func):
    def wrap():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrap

@timer
def work():
    time.sleep(5)

work()