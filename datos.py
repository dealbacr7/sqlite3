import requests
import sqlite3

conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    altura INTEGER,
    peso INTEGER,
    tipos TEXT
)
''')

limite = 1025
url_lista = f"https://pokeapi.co/api/v2/pokemon?limit={limite}"
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

            cursor.execute('''
                INSERT OR REPLACE INTO pokemon (id, nombre, altura, peso, tipos)
                VALUES (?, ?, ?, ?, ?)
            ''', (id_poke, nombre, altura, peso, tipos))
        else:
            print(f"No se pudo obtener información de {nombre}")
else:
    print("Error al obtener la lista de Pokémon.")

conn.commit()
conn.close()

print("✅ Datos guardados correctamente en 'pokemon.db'")
