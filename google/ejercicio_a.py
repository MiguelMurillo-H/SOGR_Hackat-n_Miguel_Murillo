import sys

fuente = (open(sys.argv[1], "r", encoding="utf=8") if len(sys.argv) > 1 else sys.stdin)

lineas = [line.strip() for line in fuente if line.strip()]
if not lineas:
    sys.exit(0)

T = int(lineas[0])
index = 1

for caso in range(1, T + 1):
    N = int(lineas[index])
    dados = list(map(int, lineas[index + 1].split()))
    index += 2

    dados.sort() #menor a mayor
    stair = 0 #contar la escalera consecutiva mas larga
    for _ in dados:
        if _ > stair:
            stair += 1
    print(f"Case #{caso}: {stair}")

