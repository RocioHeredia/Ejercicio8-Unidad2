from ClassConjunto import Conjunto

class Menu:

    def mostrar_menu(self):
        print("1. Unión de dos conjuntos")
        print("2. Diferencia de dos conjuntos")
        print("3. Verificar si dos conjuntos son iguales")
        print("4. Salir")

    def ejecutar_operacion(self, opcion, conjunto_a, conjunto_b):
        if opcion == 1:
            resultado = conjunto_a + conjunto_b
            print(f"La unión de {conjunto_a} y {conjunto_b} es {resultado}")
        elif opcion == 2:
            resultado = conjunto_a - conjunto_b
            print(f"La diferencia de {conjunto_a} y {conjunto_b} es {resultado}")
        elif opcion == 3:
            if conjunto_a == conjunto_b:
                print(f"{conjunto_a} y {conjunto_b} son iguales")
            else:
                print(f"{conjunto_a} y {conjunto_b} no son iguales")
        else:
            print("Opción no válida")