import sys

fuente = (open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin)

lineas = [line.strip() for line in fuente if line.strip()]
if not lineas:
    sys.exit(0)

T =int(lineas[0])
index = 1

for caso in range(1, T + 1):
    N = int(lineas[index])
    index += 1
    actividades = []
    for i in range(N):
        partes = lineas[index].split()
        s = int(partes[0])
        e = int(partes[1])
        actividades.append((s, e, i))
        index += 1
    #ordenar por minuto se inicio
    actividades.sort(key=lambda x: x[0])
    end_c = 0
    end_j = 0
    asignacion = [""] * N
    posible = True

    #Asignar a C o J segun disponibilidad
    for s, e, original_index in actividades:
        if s >= end_c:
            asignacion[original_index] = "C"
            end_c = e
        elif s >= end_j:
            asignacion[original_index] = "J"
            end_j = e
        else:
            posible = False
            break
    if posible:
        resultado = "".join(asignacion)
    else:
        resultado = "IMPOSSIBLE"
    print(f"Case #{caso}: {resultado}")
    