def f(a,b,c,d):
    return(d)

def g(a,b,c,d):
    return(0)



def deutsch_josza(fun):
   if fun(0, 0, 0, 0) == fun(0, 0, 0, 1) == fun(0, 0, 1, 1) == fun(0, 1, 1, 1) == fun(1, 1, 1, 1)== fun(1, 1, 1, 0)== fun(1, 1, 0, 0)== fun(1, 0, 0, 0):
      return 1
   else:
      return 0
   
print("deutsch-josza f:", deutsch_josza(f))
print("deutsch-josza g:", deutsch_josza(g))