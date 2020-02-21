def bignumber(arr):
    a,ans = [],''

    l = len (str(max(arr)))+1

    for i in arr:
        temp = str(i) * l
        a.append((temp[:l:],i))

    a.sort(reverse = True)

    for  i in a:

        ans+= str(i[1])

    return ans

b = list(map(int,input().split()))

print(bignumber(b))
