def doOverlap(L1, R1, L2, R2):
    if L1[0] > R2[0] or L2[0] > R1[0]:
        return 0
    if L1[1] < R2[1] or L2[1] < R1[1]:
        return 0
    return 1
        
if __name__=='__main__':
    p=[0]*2
    q=[0]*2
    r=[0]*2
    s=[0]*2
    p[0],p[1],q[0],q[1],r[0],r[1],s[0],s[1] = map(int, input().strip().split(" "))
    ans = doOverlap(p,q,r,s)
    print(ans)
