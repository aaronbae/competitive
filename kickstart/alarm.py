def build_array(N, x0, y0, C, D, E1, E2, F):
    x = [x0]
    y = [y0]
    A = [(x0+y0)%F]
    for i in range(1,N):
        x.append((C*x[i-1]+D*y[i-1]+E1) % F)
        y.append((D*x[i-1]+C*y[i-1]+E2) % F)
        A.append((x[i]+y[i])%F)
    return A

build_array(2, 1, 2, 1, 2, 1, 1, 9)        