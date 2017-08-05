import sys

sys.setrecursionlimit(100000)

cache = {}


def nextBus(now, S, F):
    if now < S:
        return S
    if (now - S) % F == 0:
        nextBus = now
    else:
        nextBus = ((now - S) / F + 1) * F + S
    return nextBus


def solve(N, Ts, Tf, buses, now, current):
    if current == N:
        if now > Tf:
            return -1
        else:
            return 0
    if (now, current) in cache:
        return cache[(now, current)]

    bus = buses[current - 1]
    S, F, D = bus
    # Let's go
    go = solve(N, Ts, Tf, buses, nextBus(now + Ts, S, F) + D, current + 1)
    # don't

    dont = solve(N, Ts, Tf, buses, nextBus(now, S, F) + D, current + 1)
    if go == -1 and dont == -1:
        cache[(now, current)] = -1
        return -1
    cache[(now, current)] = max(1 + go, dont)
    return max(1 + go, dont)


if __name__ == "__main__":
    T = input()
    for t in xrange(1, T + 1):
        cache = {}
        N, Ts, Tf = map(int, raw_input().split(" "))
        buses = []
        for _ in xrange(N - 1):
            S, F, D = map(int, raw_input().split(" "))
            buses.append((S, F, D))
        it = solve(N, Ts, Tf, buses, 0, 1)
        if it == -1:
            it = "IMPOSSIBLE"
        print "Case #{}: {}".format(t, it)
