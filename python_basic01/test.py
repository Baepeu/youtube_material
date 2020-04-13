def nCk(n, k):
    ans = 1
    for i in range(n + 1)[n:n - k:-1]:  # n*n-1*...*n-k
        ans *= i

    for i in range(k + 1)[1:]:  # k!
        ans //= i

    return ans


n, k = [int(x) for x in input().split()]

print(nCk(n, k))  # n! / ((n-k)!*k!)
