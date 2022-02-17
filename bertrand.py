# Below Is The Implementation of Bertrand's Ballot Problem : 
def factorial(p):
    prod1 = 1
    for i in range(2, p+1):
        prod1 = prod1*i
        
    return prod1
    
def comb(m, n):
    return factorial(m+n)/(factorial(m)*factorial(n))

def func(x, y, p, q,k,dp, start):
    if x>p or y>q:
        return 0
    
    if x==p and y==q:
        return 1
    
    if x-k*y<0:
        return 0
    
    if x-k*y==0 and start==False:
        return 0
        
    if dp[x][y]!=-1:
        return dp[x][y]
        
    dp[x][y]=func(x+1, y, p, q,k,dp, False) + func(x, y+1,p, q,k,dp, False)
    return dp[x][y]
    
dp = []
for i in range(0, 15):
    l1 = []
    for j in range(0, 5):
        l1.append(-1)
    dp.append(l1)
        
print(func(0,0,13,3,2,dp, True)/comb(13,3))

# Just check the printed result with : (a-k*b)/(a+b). It would match with it. This is the required probability for number of votes of A to be k times greater than
# Number of votes of B.
