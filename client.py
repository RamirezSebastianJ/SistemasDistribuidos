from xmlrpc.client import ServerProxy
a =int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el segundo numero: '))
s = ServerProxy('http://localhost:8001')
print("la suma es: " + str(s.suma(a,b)))
print("la resta es: " + str(s.resta(a,b)))
print("la multiplicacion es: " + str(s.multi(a,b)))
print("la division es: " + str(s.divi(a,b)))