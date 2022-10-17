# M=2
# V=3
#    t1,t2
# t=[1,2]
#    0,1
#    a1,a2
# t=[0.4,1]
#    0,1

def calc_x(V, M, a, t):
    x = [1] * (V + 1)
    for n in range(1, V+1):
        sum = 0
        for i in range(1, M):
            if n >= t[i]:
                sum += a[i] * t[i] * x[n - t[i]]
        x[n] = sum / n
    return x

def calc_p0(x):
    sum = 0
    for item in x:
        sum += item
    return 1 / sum

def calc_pn(x, V, M, a, t):
    P = [1] * (V + 1)
    P[0] = calc_p0(x)
    for n in range(1, V+1):
        sum = 0
        for i in range(1, M):
            if n >= t[i]:
                sum += a[i] * t[i] * P[n - t[i]]
        P[n] = sum / n
    return P


def calc_bn(P, V, t, i=1):
    sum = 0
    for n in range(V - t[i -1] + 1, V + 1):
        sum += P[n]
    return sum

def calc_all(M, V, t, a):
    x = calc_x(V, M, a, t)
    P = calc_pn(x, V, M, a, t)
    b1 = calc_bn(P, V, t, 1)
    b2 = calc_bn(P, V, t, 2)

    print("X = ", x)
    print("P = ", P)
    print("b1 = ", b1)
    print("b2 = ", b2)

M = 2
V = 3
t = [1, 2]
a = [[0.4, 1], [1, 2]]

for item in a:
    print("a =",item)
    calc_all(M, V, t, item)
    print("\n")