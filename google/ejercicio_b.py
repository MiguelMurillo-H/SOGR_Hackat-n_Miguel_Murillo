import sys

fuente = (open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin)

lineas = [line.strip() for line in fuente if line.strip()]
if not lineas:
    sys.exit(0)

#casos de prueba
T = int(lineas[0])

for caso in range(1, T + 1):
    partes = lineas[caso].split()
    X = int(partes[0])
    Y = int(partes[1])
    S = partes[2]
    INF = float("inf")
    dc = INF
    dj = INF

    for i, c in enumerate(S):
        nc = INF
        nj = INF
        if i == 0:
            if c != "J":
                nc = 0
            if c != "C":
                nj = 0
        else:
            # Si es un "C", puede venir de C, +0 o de J, +Y por JC
            if c != "J":
                nc = min(dc, dj + Y)
            #Si es "J", puede venir de J, +0 o de C, +X por CJ
            if c != "C":                    nj = min(dj, dc + X)
        dc, dj = nc, nj
    min_costo = min(dc, dj)
    print(f"Case#{caso}: {min_costo}")