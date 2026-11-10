import sys
import math

# Cubetas con capacidad, tasa de recarga por segundo, tokens actuales y último tiempo
rp = {"c": 3, "r": 1, "tok": 3.0, "l": 0}
it = {"c": 100, "r": 20, "tok": 100.0, "l": 0}

def fill(b, t):
    b["tok"] = min(b["c"], b["tok"] + b["r"] * (t - b["l"]))
    b["l"] = t

fuente = open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin

for line in fuente:
    line = line.strip().lstrip("\ufeff")
    if not line:
        continue
    partes = line.split()
    if partes[0] != "REQUEST":
        continue
    
    t = int(partes[1])
    nu = int(partes[2])
    # los de cache no gastan tokens
    
    fill(rp, t)
    fill(it, t)
    
    if rp["tok"] >= 1 and it["tok"] >= nu:
        rp["tok"] -= 1
        it["tok"] -= nu
        print("ok")
    else:
        w = 0
        if rp["tok"] < 1:
            w = max(w, math.ceil((1 - rp["tok"]) / rp["r"]))
        if it["tok"] < nu:
            w = max(w, math.ceil((nu - it["tok"]) / it["r"]))
        print(f"429 retry-after={w}")
