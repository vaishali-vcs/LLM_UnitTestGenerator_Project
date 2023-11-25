def printMultiples(n, m):
    'takes n and m as integers and finds all first m multiples of n'
    for m in (n,m):
        if n % 2 == 0:
            while n < 0:
                print(n)