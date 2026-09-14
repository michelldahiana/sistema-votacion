# Sistema de votación 

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

    print(f"Total de votos: {total_votos}\n")

    for candidato, cantidad in votos.items():
        porcentaje = (cantidad / total_votos) * 100
        barra = "█" * int(porcentaje // 5)

        print(
            f"{candidato}: {cantidad} votos | "
            f"{porcentaje:.2f}% | {barra}"
        )


def reiniciar_votacion():
    print("\n--- REINICIAR VOTACIÓN ---")
    print("Función pendiente de desarrollar.")


def menu():
    while True:
        print("\n===== SISTEMA DE VOTACIÓN =====")
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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()