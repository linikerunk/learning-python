def minimumBribes(q):
    swap = 0
    for i in range(len(q)):
        if q[i] - 1 - i >= 3:
            print("Too chaotic")
            return
    keep = True
    last_index = 0
    while keep:
        for i in range(last_index, len(q)-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                if i > 0:
                    last_index = i-1
                swap += 1
                break
        else:
            keep = False
    print(swap)
    return

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)