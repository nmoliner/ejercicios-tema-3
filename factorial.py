#generame una funcion recursiva del factorial de 5
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)


#generame una funcion iterativa del factorial de 5
def factorial_iterativo(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#generame un main para llamar a las dos funciones
def main():
    print(factorial_recursivo(5))
    print(factorial_iterativo(5))

if __name__ == "__main__":
    main()

