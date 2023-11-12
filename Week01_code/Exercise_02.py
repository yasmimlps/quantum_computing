def f(x):
    x = 0
    return x

def g(x):
    return 1 - x

def m(x):
    return x

def n(x):
    x = 1
    return x

def deutsch(fun):
   if fun(0) == fun(1):
      return 0
   else:
      return 1

print("deutsch f:", deutsch(f))
print("deutsch g:", deutsch(g))
print("deutsch m:", deutsch(m))
print("deutsch n:", deutsch(n))
