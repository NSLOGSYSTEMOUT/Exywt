

def f(n):
    return  n*n

def foo(a,b,func):
    func(a)+func(b)
    ret = func(a)+func(b)
    return ret

print(foo(1,2,f))