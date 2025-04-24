import sqlite3
import time

def mostrar_pokemones(cursor):
    inicio = time.time()
    
    cursor.execute("SELECT id, nombre, altura, peso, tipos FROM pokemon")
    pokemones = cursor.fetchall()
    
    for poke in pokemones:
        id_poke, nombre, altura, peso, tipos = poke
        print(f"ID: {id_poke} | Nombre: {nombre} | Altura: {altura} | Peso: {peso} | Tipos: {tipos}")
    
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print(f"\nEl tiempo de ejecución fue de {tiempo_transcurrido:.4f} segundos.")

def modificar_pokemon(cursor):
    id_poke = input("Ingrese el ID del Pokémon que desea modificar: ")
    campo = input("¿Qué desea modificar? (altura/peso/tipos): ").lower()
    
    if campo not in ["altura", "peso", "tipos"]:
        print("Campo no válido.")
        return

    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")

    try:
        cursor.execute(f"UPDATE pokemon SET {campo} = ? WHERE id = ?", (nuevo_valor, id_poke))
        print("Modificación realizada.")
    except sqlite3.Error as e:
        print(f"Error al modificar: {e}")

conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

while True:
    print("\nOpciones:")
    print("1. Ver todos los Pokémon")
    print("2. Modificar un Pokémon")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_pokemones(cursor)
    elif opcion == "2":
        modificar_pokemon(cursor)
        conn.commit()
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")

conn.close()
