import time


def time_it(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"Executing {func.__name__} took {t2} seconds.")

    return wrapper


@time_it
def say_moin():
    print("moin")
    time.sleep(0.7)


@time_it
def say_hi():
    print("hi")
    time.sleep(2)


say_moin()
say_hi()
print("ende")
