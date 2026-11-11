import sys

fuente = (open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin)

lineas = [line.strip() for line in fuente if line.strip()]
if not lineas:
  sys.exit(0)

T = int(lineas[0])

for caso in range(1, T + 1):
  partes = lineas[caso].split()
  N = int(partes[0])
  K = int(partes[1])

  #Conteo de intervalos de cada tamaño
  conteos = {N: 1}

  while True:
    #tomar el intervalo de mayor longitud
    x = max(conteos.keys())
    cnt = conteos.pop(x)

    #si K cae entre este grupo de intervalos
    if K <= cnt:
        max_espacio = x // 2
        min_espacio = (x - 1) // 2
        print(f"Case #{caso}: {max_espacio} {min_espacio}")
        break
    #Si no, restar cnt y dividir los intervalos
    K -= cnt
    l = x // 2
    r = (x - 1) // 2

    conteos[l] = conteos.get(l, 0) + cnt
    conteos[r] = conteos.get(r, 0) + cnt
