class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


class Agenda:
    def __init__(self, capacidad):
        self.limite = capacidad
        self.vector = [None] * capacidad
        self.contador = 0

    def registrar(self, nombre, telefono):
        if self.contador >= self.limite:
            print("Error: El vector estático está lleno.")
            return False

        self.vector[self.contador] = Contacto(nombre, telefono)
        self.contador += 1
        print(f"Sistema: Guardado en la posición [{self.contador - 1}].")
        return True

    def reporte_general(self):
        print("\n--- REPORTE GENERAL DE LA AGENDA ---")
        if self.contador == 0:
            print("No hay registros.")
            return

        for i in range(self.contador):
            print(f"Índice [{i}]: {self.vector[i].nombre} - Tel: {self.vector[i].telefono}")
        print("------------------------------------\n")

    def consultar_nombre(self, nombre_buscar):
        print(f"Consultando información para: '{nombre_buscar}'")
        encontrado = False

        for i in range(self.contador):
            if self.vector[i].nombre.lower() == nombre_buscar.lower():
                print(f"-> Encontrado en Índice [{i}]: Tel: {self.vector[i].telefono}")
                encontrado = True

        if not encontrado:
            print("No se encontraron coincidencias.")


if __name__ == "__main__":
    mi_agenda = Agenda(5)

    mi_agenda.registrar("Sergio", "0991234567")
    mi_agenda.registrar("Carlos", "0987654321")
    mi_agenda.registrar("Maria", "0955556666")

    # Ejecución de funcionalidades obligatorias
    mi_agenda.reporte_general()
    mi_agenda.consultar_nombre("Sergio")
