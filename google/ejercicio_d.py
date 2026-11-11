import sys

fuente = (open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin)

lineas = [line.strip() for line in fuente if line.strip()]
if not lineas:
    sys.exit(0)

T = int(lineas[0])
index = 1

for caso in range(1, T + 1):
    N = int(lineas[index])
    F = list(map(int, lineas[index + 1].split()))
    P = list(map(int, lineas[index + 2].split()))
    index += 3

    #Construir la lista de hijos para cada nodo
    hijos = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        hijos[P[i - 1]].append(i)
    car = [0] * (N + 1)
    tot = 0

    #desde N hasta 1
    for i in range(N, 0, -1):
        if not hijos[i]:
            car[i] = F[i - 1]
        else:
            m = float("inf")
            s = 0
            for k in hijos[i]:
                s += car[k]
                if car[k] < m:
                    m = car[k]
            tot += s - m
            car[i] = max(F[i -1], m)
    
    #sumar los iniciadores que llegan al abismo
    for k in hijos[0]:
        tot += car[k]
    
    print(f"Case #{caso}: {tot}")