from Controlador import ControladorCuerpo
from Controlador.ControladorSoldado import ControladorSoldado
from Controlador.ControladorCuartel import ControladorCuartel
from Modelo.Infanteria import Infanteria
from Modelo.Artilleria import Artilleria
from Modelo.Armada import Armada
from Vista.VistaSoldado import VistaSoldado
from Vista.VistaCuartel import VistaCuartel

class VistaCuerpo:

    controladorSoldado = ControladorSoldado()
    vistaSoldado = VistaSoldado(controladorSoldado)

    controladorCuartel = ControladorCuartel()
    vistaCuartel = VistaCuartel(controladorCuartel)


    def __init__(self, controladorCuerpo: ControladorCuerpo):
        self.controladorCuerpo = controladorCuerpo
        self.archivo = "cuerpos.json"
        self.cargarCuerpos()
        self.vistaSoldado.cargarSoldados()


    def menu(self):
        while True:
            self.mostrar_menu()
            opcion = self.obtener_opcion_usuario()
            if opcion == 1:
                self.crearCuerpo()
            elif opcion == 2:
                self.listarCuerpos()
            elif opcion == 3:
                self.buscarCuerpo()
            elif opcion == 4:
                self.actualizarCuerpo()
            elif opcion == 5:
                self.eliminarCuerpo()
            elif opcion == 6:
                self.agregarSoldadoCuerpo()
            elif opcion == 7:
                self.eliminarSoldadoCuerpo()
            elif opcion == 8:
                print("Saliendo del menú...")
                break
            else:
                print("Opción no válida, por favor elija una opción del 1 al 8.")

    def mostrar_menu(self):
        print("\nCUERPO")
        print("1. Crear Cuerpo")
        print("2. Listar Cuerpos")
        print("3. Buscar Cuerpo")
        print("4. Actualizar Cuerpo")
        print("5. Eliminar Cuerpo")
        print("6. Agregar Soldado a Cuerpo")
        print("7. Eliminar Soldado de Cuerpo")
        print("8. Salir")

    def obtener_opcion_usuario(self) -> int:
        while True:
            try:
                return int(input("Elija una opción: "))
            except ValueError:
                print("Error: Ingrese un número válido.")

    def crearCuerpo(self):
        tipo = input("Ingrese el tipo de Cuerpo (Infanteria, Artilleria, Armada): ").lower()
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        nombre = input("Ingrese el nombre del Cuerpo: ")
        descripcion = input("Ingrese la descripción del Cuerpo: ")

        if tipo == 'infanteria':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, especialidad): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, tipo de combate): ")
            cuerpo = Infanteria(idCuerpo, nombre, descripcion, atributo1, atributo2)
        elif tipo == 'artilleria':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, tipo de artillería): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, equipo necesario): ")
            cuerpo = Artilleria(idCuerpo, nombre, descripcion, atributo1, atributo2)
        elif tipo == 'armada':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, tipo de nave): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, capacidad): ")
            cuerpo = Armada(idCuerpo, nombre, descripcion, atributo1, atributo2)
        else:
            print("Tipo de cuerpo no válido.")
            return

        self.controladorCuerpo.create(cuerpo)
        print("Cuerpo creado exitosamente.")
        self.guardarCuerpos()

    def listarCuerpos(self):
        cuerpos = self.controladorCuerpo.index()
        if cuerpos:
            for cuerpo in cuerpos:
                print(cuerpo.toStr())
        else:
            print("No hay cuerpos registrados.")

    def buscarCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        cuerpo = self.controladorCuerpo.get(idCuerpo)
        if cuerpo:
            print(cuerpo.toStr())
        else:
            print("Cuerpo no encontrado.")

    def actualizarCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        tipo = input("Ingrese el nuevo tipo de Cuerpo (Infanteria, Artilleria, Armada): ").lower()
        nombre = input("Ingrese el nuevo nombre del Cuerpo: ")
        descripcion = input("Ingrese la nueva descripción del Cuerpo: ")

        if tipo == 'infanteria':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, especialidad): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, tipo de combate): ")
            cuerpo = Infanteria(idCuerpo, nombre, descripcion, atributo1, atributo2)
        elif tipo == 'artilleria':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, tipo de artillería): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, equipo necesario): ")
            cuerpo = Artilleria(idCuerpo, nombre, descripcion, atributo1, atributo2)
        elif tipo == 'armada':
            atributo1 = input("Ingrese el primer atributo adicional (por ejemplo, tipo de nave): ")
            atributo2 = input("Ingrese el segundo atributo adicional (por ejemplo, capacidad): ")
            cuerpo = Armada(idCuerpo, nombre, descripcion, atributo1, atributo2)
        else:
            print("Tipo de cuerpo no válido.")
            return

        cuerpo_actualizado = self.controladorCuerpo.update(cuerpo)
        if cuerpo_actualizado:
            print("Cuerpo actualizado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def eliminarCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        eliminado = self.controladorCuerpo.delete(idCuerpo)
        if eliminado:
            print("Cuerpo eliminado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def agregarSoldadoCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        idSoldado = input("Ingrese el ID del Soldado: ")

        soldado = self.controladorSoldado.get(idSoldado)
        cuerpo = self.controladorCuerpo.get(idCuerpo)

        if cuerpo is not None:
            cuerpo.agregarSoldado(soldado)
            print("Soldado agregado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def eliminarSoldadoCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        idSoldado = input("Ingrese el ID del Soldado: ")

        cuerpo = self.controladorCuerpo.get(idCuerpo)
        if cuerpo is not None:
            cuerpo.eliminarSoldado(idSoldado)
            print("Soldado eliminado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def agragarCuartelCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        idCuartel = input("Ingrese el ID del Cuartel: ")

        cuartel = self.controladorCuartel.get(idCuartel)
        cuerpo = self.controladorCuerpo.get(idCuerpo)

        if cuerpo is not None:
            cuerpo.agregarCuartel(cuartel)
            print("Cuartel agregado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def eliminarCuartelCuerpo(self):
        idCuerpo = input("Ingrese el ID del Cuerpo: ")
        idCuartel = input("Ingrese el ID del Cuartel: ")

        cuerpo = self.controladorCuerpo.get(idCuerpo)
        if cuerpo is not None:
            cuerpo.eliminarCuartel(idCuartel)
            print("Cuartel eliminado exitosamente.")
            self.guardarCuerpos()
        else:
            print("Cuerpo no encontrado.")

    def guardarCuerpos(self):
        self.controladorCuerpo.guardar(self.archivo)

    def cargarCuerpos(self):
        self.controladorCuerpo.cargar(self.archivo)
