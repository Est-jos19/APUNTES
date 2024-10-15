print ("Serie de Fibonacci")
fnp, fn = 1, 1
#
n = input("Tope de Fn")
n = int(n)
#
if n==0:
    print("[1]")
elif n==1:
    print("[1, 1]")
    
##
else:
    output = "[1, 1"
    for i in range(2, n+1):
        tmp = fn[-1] + fn[-2]
        fn.append(tmp)
        
    #
    outpu= ""
    
        
##
    output += "]"
    print(output)
    