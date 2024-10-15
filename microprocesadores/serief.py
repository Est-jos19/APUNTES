import time 
print ("Serie de Fibonacci")

k = int(input("¿Qué valor de k quieres?:"))
#
n=2
i=2
r=1
while r==1:
       
##
    if i<n+1:
        x = [1, 1]
        for i in range( n+1):
            tmp = x[-2] + x[-1]
            
            
            x.append(tmp)
            
            if x[-1]/ 10**(k-1) >= 1:
                print(x)
                print(f"[{x[-1]}]")
                r=0
                
        n+=1
        i+=1
            
            
        
        
##
    
    
    