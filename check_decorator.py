from cache_decorator_m import cache_decorator

@cache_decorator
def greet(name):
    return "hello {}".format(name)
@cache_decorator
def hello_world():
    return "hello World!"
@cache_decorator
def calculate_pow(num,Pows):#very stupid pow calculation
    sum=1
    for i in range(Pows):
        sum=sum*num
    return sum
if __name__=="__main__":
    print(greet("michal"))
    print(greet("nir"))
    print(greet("michal",use_cache=False))
    print(greet("nir"))
    print(calculate_pow(5,7))
    print(calculate_pow(5,7))
    print(calculate_pow(5,8))
    print(hello_world())
    print(hello_world())
    