import hashlib
def cache_decorator(fn):
    cache = {}

    def wrapper(*args ,use_cache=True, **kwargs):
        nonlocal cache
        args_str = ', '.join(str(arg) for arg in args)
        kwargs_str = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        cur_fn = "{}({})".format(fn.__name__, ', '.join([args_str, kwargs_str]))
        hash_key = hashlib.sha256(cur_fn.encode()).hexdigest()#im using hashing incase the function call gets very long

        if hash_key in cache and use_cache==True :
            print("this what ive found in cache :")
            return cache[hash_key]
        
        else:
            print("not in cache")
            result=fn(*args,**kwargs)    
            cache[hash_key]=result
            return result    
    return wrapper




