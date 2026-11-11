import sys
import json

CLIMAS = {"Bogotá": "14 °C", "Medellín": "24 °C", "Cali": "26 °C"}
total_llamadas = 0
total_errores = 0

fuente = open(sys.argv[1], "r", encoding="utf-8") if len(sys.argv) > 1 else sys.stdin

for line in fuente:
    line = line.strip().lstrip("\ufeff")
    if not line:
        continue
    data = json.loads(line)
    stop_reason = data.get("stop_reason")

    # Si pide herramientas
    if stop_reason == "tool_use":
        for item in data.get("content", []):
            if item.get("type") == "tool_use":
                tid = item["id"]
                name = item["name"]
                inpt = item.get("input", {})
                resultado = ""

                # calculadora
                if name == "calculadora":
                    operation = inpt.get("operacion")
                    a, b = inpt.get("a", 0), inpt.get("b", 0)
                    if operation == "sumar":
                        resultado = str(a + b)
                    elif operation == "restar":
                        resultado = str(a - b)
                    elif operation == "multiplicar":
                        resultado = str(a * b)
                    elif operation == "dividir":
                        resultado = "error: división por cero" if b == 0 else str(int(a / b))
                    else:
                        resultado = f"error: operación desconocida: {operation}"

                # clima
                elif name == "clima":
                    ciudad = inpt.get("ciudad", "")
                    if ciudad in CLIMAS:
                        resultado = CLIMAS[ciudad]
                    else:
                        resultado = f"error: ciudad desconocida: {ciudad}"

                # herramienta desconocida
                else:
                    resultado = f"error: herramienta desconocida: {name}"

                total_llamadas += 1
                if resultado.startswith("error:"):
                    total_errores += 1

                print(f"tool_result {tid} {resultado}")

    # mensaje final
    elif stop_reason == "end_turn":
        for item in data.get("content", []):
            if item.get("type") == "text":
                print(f"final: {item['text']}")

# resumen
print(f"resumen: {total_llamadas} llamadas, {total_errores} errores")
