"""1a"""
class Palindromo:
    def esPalindromo(cls, cadena):
        # Eliminar caracteres no alfanuméricos y convertir a minúsculas
        cadena = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
        # Verificar si la cadena es igual a su inverso
        return cadena == cadena[::-1]

# Ejemplos de uso
print(Palindromo.esPalindromo('radar')) 
print(Palindromo.esPalindromo('sonar')) 
print(Palindromo.esPalindromo('Arde ya la yedra')) 
print(Palindromo.esPalindromo('Ardeyalayedra')) 
print(Palindromo.esPalindromo('!@#$% %$#@!')) 
print(Palindromo.esPalindromo('L O L'))

"""b"""
