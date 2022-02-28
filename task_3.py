from textwrap import wrap
from typing import Counter
from functools import wraps


def counter (function_decorate):
    @wraps (function_decorate)
    def wrap (*args, **qwargs):
        print (f'args: {args}')
        print (f'qwargs: {qwargs}')
        print (f'retvalue: {function_decorate(*args, **qwargs)}')
        return print(function_decorate(*args, **qwargs))
    return wrap

@ counter
def consat (*args, revers=False):
    if revers:
        args = reversed(args)
    result, *other = args
    for num in other:
        result += num
    return result

consat ('hello', ' ','world')
consat ('hello', ' ','world', revers=True)
