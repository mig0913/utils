from decoratorme import timeit
from decoratorme import print_args
import time

@timeit
def my_function():
    time.sleep(3)

@timeit
@print_args
def generate_report(*months,**para):
    time.sleep(2)
    print ('(actual function) Done, report links ...')

para = dict(lastname = 'Arias',First='Miguel')
generate_report(range(1,10), para)
