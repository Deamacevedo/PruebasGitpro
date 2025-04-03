from archivo_json import cargar_datos, guardar_datos

ARTISTAS_JSON = "data/artistas.json"

def agregar_artista():
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("Nombre del artista: ").strip()
    pais = input("País de origen: ").strip()
    años_actividad = input("Años de actividad: ").strip()
    año_lanzamiento = input("Año de lanzamiento del primer disco: ").strip()
    genero = input("Género musical: ").strip()
    unidades_certificadas = input("Unidades certificadas totales: ").strip()
    ventas_reclamadas = input("Ventas reclamadas: ").strip()
    estado = input("¿El artista sigue activo? (Sí/No): ").strip()

    nuevo_artista = {
        "Artist name": nombre,
        "Country": pais,
        "Active years": años_actividad,
        "Release year of first charted record": int(año_lanzamiento),
        "Genre": genero,
        "Total certified units": unidades_certificadas,
        "Claimed sales": ventas_reclamadas,
        "Active": estado.lower() == "sí"
    }

    artistas.append(nuevo_artista)
    guardar_datos(ARTISTAS_JSON, artistas)
    print(" Artista agregado correctamente.")

def mostrar_artistas():
    artistas = cargar_datos(ARTISTAS_JSON)
    
    if not artistas:
        print("No hay artistas registrados.")
        return

    print("\n🎵 Lista de Artistas:")
    for artista in artistas:
        print(f"- {artista['Artist name']} ({artista['Country']}) - Género: {artista['Genre']}")

def editar_artista():
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("Ingrese el nombre del artista a editar: ").strip()
    artista = next((a for a in artistas if a["Artist name"].lower() == nombre.lower()), None)

    if not artista:
        print("❌ Artista no encontrado.")
        return

    print(f"🎵 Editando artista: {artista['Artist name']}")

    artista["Country"] = input(f"Nuevo país ({artista['Country']}): ").strip() or artista["Country"]
    artista["Active years"] = input(f"Nuevos años de actividad ({artista['Active years']}): ").strip() or artista["Active years"]
    artista["Release year of first charted record"] = int(input(f"Nuevo año de lanzamiento ({artista['Release year of first charted record']}): ").strip() or artista["Release year of first charted record"])
    artista["Genre"] = input(f"Nuevo género ({artista['Genre']}): ").strip() or artista["Genre"]
    artista["Total certified units"] = input(f"Nuevas unidades certificadas ({artista['Total certified units']}): ").strip() or artista["Total certified units"]
    artista["Claimed sales"] = input(f"Nuevas ventas reclamadas ({artista['Claimed sales']}): ").strip() or artista["Claimed sales"]
    artista["Active"] = input(f"¿Sigue activo? ({'Sí' if artista['Active'] else 'No'}): ").strip().lower() == "sí"

    guardar_datos(ARTISTAS_JSON, artistas)
    print("✅ Artista editado correctamente.")

def eliminar_artista():
    """Elimina un artista de la base de datos."""
    artistas = cargar_datos(ARTISTAS_JSON)

    nombre = input("Ingrese el nombre del artista a eliminar: ").strip()
    artistas_filtrados = [a for a in artistas if a["Artist name"].lower() != nombre.lower()]

    if len(artistas) == len(artistas_filtrados):
        print("❌ Artista no encontrado.")
        return

    guardar_datos(ARTISTAS_JSON, artistas_filtrados)
    print("✅ Artista eliminado correctamente.")
