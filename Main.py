from ClassConjunto import Conjunto
from ClassMenu import Menu

def test():
    menu = Menu()
    conjunto_a = Conjunto([1, 2, 3, 4])
    conjunto_b = Conjunto([3, 6, 9])

    while True:
        menu.mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 4:
            break
        menu.ejecutar_operacion(opcion, conjunto_a, conjunto_b)


if __name__ == "__main__":
    test()