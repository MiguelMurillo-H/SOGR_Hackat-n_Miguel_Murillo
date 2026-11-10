import sys
import json

bloques = {}
input_tokens = 0
output_token = 0
stop_reason = ""

for line in sys.stdin:
    line = line.strip()
    if not line.startswith("data:"):
        continue
    content = line[5:].strip()
    try:
        data = json.loads(content)
    except:
        continue
    tipo = data.get("type")

    #Guardar los input tokens al iniciar el mensaje
    if tipo == "message_start":
        bloques = {}
        input_tokens = data["message"]["usage"]["input_tokens"]
    
    #guardar el pedazo de texto segun su bloqu
    elif tipo == "content_block_delta":
        index = data["index"]
        delta = data.get("delta", {})
        if delta.get("type") == "text_delta":
            bloques[index] = bloques.get(index, "") + delta.get("text", "")
    
    #guardar los output tokens al finalizar el mensaje, con el motivo
    elif tipo == "message_delta":
        stop_reason = data["delta"]["stop_reason"]
        output_token = data["usage"]["output_tokens"]
    
    #Al finalizar el mensaje, imprimir los resultados
    elif tipo == "message_stop":
        texto_completo = "".join(bloques[i] for i in sorted(bloques.keys()))
        print(f"texto: {texto_completo}")
        print(f"stop_reason: {stop_reason}")
        print(f"input_tokens: {input_tokens}")
        print(f"output_tokens: {output_token}")