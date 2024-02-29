while True:
    try:
        A, B = map(int, input().split())
        print(abs(A-B))
    except:
        break
