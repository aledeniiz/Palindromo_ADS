class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena

    @staticmethod
    def esPalindromo(cadena):
        cadena = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
        return cadena == cadena[::-1]

    def test(self):
        return self.esPalindromo(self.cadena)

    def __del__(self):
        print(self.cadena.upper())

p = Palindromo("radar")
print(p.test())  # True

p = Palindromo("sonar")
print(p.test())  # False

"""Muestra radar cuando se crea el palindromo sonar porque al poner el el nuevo valor para p segun esta programado hay que printear su ultimo 
valor en mayusculas"""