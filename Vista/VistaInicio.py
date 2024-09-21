from Controlador.ControladorMinisterio import ControladorMinisterio
from Vista.VistaMinisterio import VistaMinisterio

from Controlador.ControladorCuerpo import ControladorCuerpo
from Vista.VistaCuerpo import VistaCuerpo

from Controlador.ControladorSoldado import ControladorSoldado
from Vista.VistaSoldado import VistaSoldado

from Controlador.ControladorCuartel import ControladorCuartel
from Vista.VistaCuartel import VistaCuartel

from Controlador.ControladorCompania import ControladorCompania
from Vista.VistaCompania import VistaCompania

from Controlador.ControladorDespliegue import ControladorDespliegue
from Vista.VistaDespliegue import VistaDespliegue

from Controlador.ControladorServicio import ControladorServicio
from Vista.VistaServicio import VistaServicio

from Controlador.ControladorServicioRealizado import ControladorServicioRealizado
from Vista.VistaServicioRealizado import VistaServicioRealizado

class VistaInicio:
    def __init__(self):
        pass

    def menu(self):
        while True:
            print("\nMINISTERIO DE DEFENSA NACIONAL")
            print("\nMenú Principal")
            print("1. Ir a Menú de Ministerio")
            print("2. Ir a Menú de Cuerpo")
            print("3. Ir a Menú de Soldado")
            print("4. Ir a Menú de Cuartel")
            print("5. Ir a Menú de Compañía")
            print("6. Ir a Menú de Despliegue")
            print("7. Ir a Menú de Servicio")
            print("8. Ir a Menú de Servicio Realizado")
            print("9. Salir")
            opcion = input("Elija una opción: ")

            if opcion == '1':
                controladorministerio = ControladorMinisterio()
                vistaMinisterio = VistaMinisterio(controladorministerio)
                vistaMinisterio.menu()  # Regresar al menú de ministerios
            elif opcion == '2':
                controladorcuerpo = ControladorCuerpo()
                vistaCuerpo = VistaCuerpo(controladorcuerpo)
                vistaCuerpo.menu()
            elif opcion == '3':
                controladorsoldado = ControladorSoldado()
                vistasoldado = VistaSoldado(controladorsoldado)
                vistasoldado.menu()
            elif opcion == '4':
                controladorcuartel = ControladorCuartel()
                vistacuartel = VistaCuartel(controladorcuartel)
                vistacuartel.menu()
            elif opcion == '5':
                controladorcompania = ControladorCompania()
                vistacompania = VistaCompania(controladorcompania)
                vistacompania.menu()
            elif opcion == '6':
                controladordespliegue = ControladorDespliegue()
                vistadespliegue = VistaDespliegue(controladordespliegue)
                vistadespliegue.menu()
            elif opcion == '7':
                controladroserivicio = ControladorServicio()
                vistaservicio = VistaServicio(controladroserivicio)
                vistaservicio.menu()
            elif opcion == '8':
                controladorServicioRealizado = ControladorServicioRealizado()
                vistaServicioRealizado = VistaServicioRealizado(controladorServicioRealizado)
                vistaServicioRealizado.menu()
            elif opcion == '9':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, por favor elija una opción del 1 al 9.")
