from functools import wraps
import time



def mydecorator(function):
   @wraps(function)
   def wrapper(*args,**kwargs):
       result = function(*args,**kwargs)
       return result
   return wrapper

def timeit(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print ('**** Starting Timer ****')
        start = time.time()
        
        func(*args,**kwargs)
        
        end = time.time()
        print (f'=== {func.__name__} took {int(end-start)} seconds to complete')
    return wrapper



def print_args(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print ()
        print('***args:')
        for arg in args:
            print (f' - {arg}')
        print ('***** kwargs:')
        
        for k,v in kwargs.items():
            print (f'- {k}:{v})')
        print ()

        func(*args,**kwargs)
    return wrapper 
   
