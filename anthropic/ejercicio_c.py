import sys
import json

def usd(m):
    entero = int(m // 1_000_000)
    decimal = int(m % 1_000_000)
    return f"${entero}.{decimal:06d}"

total = 0
sin_cache = 0
aciertos = 0
total_solicitudes = 0

fuente = open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin

for i, line in enumerate(fuente, start=1):
    line = line.strip().lstrip("\ufeff")
    if not line:
        continue
    u = json.loads(line)
    inp = u.get("input_tokens", 0)
    c_crea = u.get("cache_creation_input_tokens", 0)
    c_read = u.get("cache_read_input_tokens", 0)
    out = u.get("output_tokens", 0)
    
    c = (inp * 300 + c_crea * 375 + c_read * 30 + out * 1500) // 100
    n = (inp + c_crea + c_read) * 3 + out * 15
    
    total += c
    sin_cache += n
    if c_read > 0:
        aciertos += 1
    total_solicitudes += 1
    print(f"solicitud {i}: {usd(c)}")

ahorro = sin_cache - total
print(f"total: {usd(total)}")
print(f"sin_cache: {usd(sin_cache)}")
print(f"ahorro: {usd(ahorro)}")
print(f"aciertos_de_cache: {aciertos}/{total_solicitudes}")
