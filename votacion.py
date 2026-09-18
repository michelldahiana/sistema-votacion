# Sistema de votación mejora: resultados con porcentajes y barras visuales

votos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0
}

personas_votaron = {}


def registrar_voto():
    print("\n--- REGISTRAR VOTO ---")

    identificacion = input("Ingrese su número de identificación: ")

    if identificacion in personas_votaron:
        print("Esta persona ya realizó su voto.")
        return

    print("\nCandidatos disponibles:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")

    opcion = input("Seleccione un candidato: ")

    candidatos = {
        "1": "Candidato A",
        "2": "Candidato B",
        "3": "Candidato C"
    }

    if opcion not in candidatos:
        print("Opción inválida.")
        return

    candidato = candidatos[opcion]

    votos[candidato] += 1
    personas_votaron[identificacion] = candidato

    print("Voto registrado correctamente.")


def ver_resultados():
    print("\n--- RESULTADOS DE LA VOTACIÓN ---")

    total_votos = sum(votos.values())

    if total_votos == 0:
        print("Todavía no hay votos registrados.")
        return

    print(f"Total de votos: {total_votos}")
    print("Porcentajes de cada candidato:\n")

    for candidato, cantidad in votos.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"{candidato}: {cantidad} votos - {porcentaje:.2f}%")

    # Mejora adicional: mostrar el ganador
    mayor_votos = max(votos.values())

    ganadores = [
        candidato
        for candidato, cantidad in votos.items()
        if cantidad == mayor_votos
    ]

    if len(ganadores) == 1:
        print(f"\n🏆 El ganador es: {ganadores[0]}")
    else:
        print(f"\n🤝 Hay un empate entre: {', '.join(ganadores)}")


from datetime import datetime


def reiniciar_votacion():
    print("\n--- REINICIAR VOTACIÓN ---")

    confirmacion = input(
        "¿Está seguro de reiniciar la votación? (si/no): "
    ).lower()

    if confirmacion != "si":
        print("Operación cancelada.")
        return

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_votos = sum(votos.values())

    with open("historial_votaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n--- Votación finalizada: {fecha} ---\n")

        for candidato, cantidad in votos.items():
            archivo.write(f"{candidato}: {cantidad} votos\n")

        archivo.write(f"Total de votos: {total_votos}\n")

    for candidato in votos:
        votos[candidato] = 0

    personas_votaron.clear()

    print("Votación reiniciada.")
    print("Historial guardado en historial_votaciones.txt")


    
while True:
    print("\n==============================")
    print("     SISTEMA DE VOTACIÓN")
    print("==============================")
    print("1. Registrar voto")
    print("2. Ver resultados")
    print("3. Reiniciar votación")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_voto()
    elif opcion == "2":
        ver_resultados()
    elif opcion == "3":
        reiniciar_votacion()
    elif opcion == "4":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

