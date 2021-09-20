def task1(n:int, k:int) -> int:
    if k>=n:
        return 0

    count = n-k
    for i in range(k+1, n+1):
        j = 1
        while i*j + k<=n:
            count +=1
            j +=1

    return count
if __name__ == '__main__':
    n = 5
    k = 2
    print(task1(5,2))
