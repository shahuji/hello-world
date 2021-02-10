# use of Lamda Function

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


# Applying decorator to a function
@trace
def add_two(x):
    # print("X is: ", x+2)
    return x + 2


# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))
