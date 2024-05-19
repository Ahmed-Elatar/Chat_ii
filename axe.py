from operator import itemgetter
def maxPointsInsideSquare( points,s):
    n=len(s)
    s=[*s]
    lst=[]
    ans=[]
    ans2=[]
    for i in range(0,n):
        lst.append([points[i][0],points[i][1],max(abs(points[i][0]),abs(points[i][1])),s[i]])

    # lst = sorted(points, key=itemgetter(2))
    lst.sort(key=lambda elem: elem[2])
    cnt=0
    cr=100000000000000000000
    for i in lst:
        if i[3] not in ans2:
            ans.append (i)
            ans2.append(i[3])
        else:
            cr=i[2]
            break
    for i in ans:
        if i[2] ==cr:
            cnt+=1
    return len(ans)-cnt
    # return lst




    


points = [[0,-4],[0,0]]
s="fabccddg"



print(maxPointsInsideSquare(points,s))