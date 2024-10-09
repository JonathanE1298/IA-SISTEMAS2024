#Ejercicio 6
def fibonacci(n):
    x,y, aux = 0,1,0

                                                        
    for i in range(n):
        print(x, end=", ")
        aux = x
        x = y
        y = aux + y
    print()

n = 7
print("Serie de Fibonacci:")
fibonacci(n)