#def factors(num):
#    factorlist = []
#    for i in range(1,num+1):
#        if num % i == 0:
#            factorlist.append(i)
#    return factorlist
            
def factors(num):
    factorlist = []
    for i in range(1,num+1):
        if num % i == 0:
            factorlist.append(i)
    return factorlist

def gcf(a,b): #find the Greatest common factor of two numbers a & b
    gcflist = []    # define lists
    alist = []
    blist = []
    for i in range(1,a+1):  #find factors of a and put them in a list
        if a % i == 0:
            alist.append(i)
    for i in range(1,b+1):    #find factors of b and put them in b list
        if b % i == 0:
            blist.append(i)
    for f in alist:     # compare numbers in alist and blist and if the number in a list is in blist then append that number to gcflist
        if f in blist:
            gcflist.append(f)
    return max(gcflist) # or gcflist[-1]



