## k digito de fibonacci
import time 
def Fib(fnp, fn, i):
    n=3
    while 1:
        if i<n:
            Fib(fnp+fn, fnp,i+1)
            
        n+=1
        time.sleep(1)
        print(fnp)
    
    
Fib(1, 1, 2)