import requests
import time

limite = 1025
url_lista = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"

inicio = time.time()

respuesta = requests.get(url_lista)

if respuesta.status_code == 200:
    datos = respuesta.json()
    resultados = datos["results"]

    for pokemon in resultados:
        nombre = pokemon["name"]
        url_detalle = pokemon["url"]

        detalle = requests.get(url_detalle)
        if detalle.status_code == 200:
            info = detalle.json()
            id_poke = info["id"]
            altura = info["height"]
            peso = info["weight"]
            tipos = ', '.join([tipo["type"]["name"] for tipo in info["types"]])

            print(f"ID: {id_poke} | Nombre: {nombre} | Altura: {altura} | Peso: {peso} | Tipos: {tipos}")
        else:
            print(f"No se pudo obtener detalles de {nombre}")
else:
    print("No se pudo acceder a la API.")

fin = time.time()

tiempo_transcurrido = fin - inicio
print(f"\nEl tiempo de ejecución fue de {tiempo_transcurrido:.4f} segundos.")
