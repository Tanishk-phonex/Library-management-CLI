from functools import wraps
import time
def logger(filee):
    def innerdeco(func):
        @wraps(func)
        def wrapper(*args):
            v=func(*args)
            with open(filee,"a") as f:
                f.write(f"output of function {func.__name__} : {v} \n")
            return v
        return wrapper
    return innerdeco

def retry(tries=3):
    def innerdeco(func):
        @wraps(func)
        def wrapper(*args):
            for i in range(tries):
                try:
                    return func(*args)
                except:
                    print(f"Attempt {i+1} failed : left {tries - i-1}")
            print("All attempts failed")
        return wrapper
    return innerdeco

def delay(n):
    def innerdeco(func):
        @wraps(func)
        def wrapper(*args):
            time.sleep(n)
            return func(*args)
        return wrapper
    return innerdeco

def timeit(func):
    @wraps(func)
    def wrapper(*args):
        s=time.time()
        v=func(*args)
        e=time.time()
        print(f"funtion ran in {e-s} seconds ")
        return v
    return wrapper

def secure(func):
    @wraps(func)
    def wrapper(*args):
        while True:
            a=input("enter password")
            if a== "02042007":
                return func(*args)
            
            else:
                print("INCORRECT PASSWORD 'check README.md in #notes'")
    return wrapper

