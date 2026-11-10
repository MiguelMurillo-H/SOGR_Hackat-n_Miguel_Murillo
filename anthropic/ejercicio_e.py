import sys
import json
import re
import unicodedata

def enorm(s):
    #Normalizar NFD para quitar tildes
    s = unicodedata.normalize('NFD', str(s))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.lower()
    #Todo lo que no sea letra o numero se vuelve espacio
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return s.strip()

categorias = {}
total_aprobadas = 0
total_casos = 0

fuente = open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin

for line in fuente:
    line = line.strip().lstrip("\ufeff")
    if not line:
        continue
    data = json.loads(line)
    cat = data["categoria"]
    esp = data["esperado"]
    res = data["respuesta"]
    
    #Comprobar si 'esperado' aparece como palabra(s) completa(s)
    pass_ok = f" {enorm(esp)} " in f" {enorm(res)} "
    
    if cat not in categorias:
        categorias[cat] = [0, 0]  #[aprobadas, total]
    categorias[cat][1] += 1
    total_casos += 1
    
    if pass_ok:
        categorias[cat][0] += 1
        total_aprobadas += 1

#Imprimir por categoria en orden alfabetico
for cat in sorted(categorias.keys()):
    aprobadas, total = categorias[cat]
    print(f"{cat}: {aprobadas}/{total}")

porcentaje = (total_aprobadas / total_casos) * 100 if total_casos > 0 else 0.0
print(f"total: {total_aprobadas}/{total_casos} ({porcentaje:.1f}%)")
