def send_gen():
    while True:
        x = yield
        print("Received:", x)

gen = send_gen()
next(gen)
gen.send("Hello")