
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))

"""El resultado <class '__main__.A'> indica que la clase A está definida en el módulo principal (__main__). 
wCuando Python ejecuta un script directamente, el módulo principal se llama __main__. Por lo tanto, cuando se imprime una referencia a la clase A, s
e muestra esta representación. Esto se debe a que al asignar a = A, a se convierte en una referencia a la clase A."""

"""Devuelve False debido a que afirma que aa es igual a a(), y no lo es"""

"""Devuelve 0 porque se llama al método y de aa con una tupla vacía"""

"""Devuelve 1 porque la longitud de la tupla de print(a().y((a,))) es 1"""

"""Devuelve 2 porque la tupla tiene un elemento mas que la anterior"""

"""Devuelve 3 por la misma razon que el elemento anterior"""