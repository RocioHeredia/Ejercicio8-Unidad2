class Conjunto:

    def __init__(self, elementos):
        self.__elementos = set(elementos)

    def __add__(self, otro_conjunto):
        resultado = {elemento for conjunto in (self.__elementos, otro_conjunto.__elementos) for elemento in conjunto}
        return resultado

    def __sub__(self, otro_conjunto):
        resultado = {elemento for elemento in self.__elementos if elemento not in otro_conjunto.__elementos}
        return Conjunto(resultado)

    def __eq__(self, otro_conjunto):
        if len(self.__elementos) == len(otro_conjunto.__elementos):
            return self.__elementos == otro_conjunto.__elementos
        
    def __str__(self) -> str:
        return f"{self.__elementos}"