def sockMerchant(n, ar):
    sock_array=ar
    matches=0
    if n==1:
        return(0)
    for l in range(n):
        sock_counter=1
        for i in ar:
            for m in ar[sock_counter:]:
                if i==m:
                    matches=matches+1
                    ar.remove(i)
                    ar.remove(m)
                    break
            if i==m:
                break
            sock_counter=sock_counter+1
        if i==m and sock_counter==len(sock_array):
            break
    return(matches)

ar=[10, 10, 10, 20, 30, 30, 30, 40, 40]
n=len(ar)
print(sockMerchant(n, ar))
