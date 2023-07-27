# cache-decorator
python decorator with caching capabilities.

## How to use
Basically import the decorator function from module and add it 
to any function which returns something to cache.
the use_cache is set to use by default, and checks whether the function ran before
and returns the cache value if it did. if value "False" is passed to function
call the fuction will be called, the value is being cached anyway.

## add a decorator example
```python
from cache_decorator_m import cache_decorator
@cache_decorator
def greet(name):
    return "hello {}".format(name)
```
## call the decorator without cache
```python
print(greet("michal",use_cache=False))
```
### output
```
not in cache
hello michal
```
## call the decorator with cache right after
```python
print(greet("michal",use_cache=False))
print(greet("michal",use_cache=True))
```
### output
```
not in cache
hello michal
this what ive found in cache :
hello michal
```


## List of files:
    cache_decorator_m.py : cache decorator module.
    check_decorator.py : just an example use of file.