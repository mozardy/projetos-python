def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number or number == 0


# Teste com um número qualquer
numero_teste = int(input('Digite um número: '))

if is_fibonacci(numero_teste):
    print(f"O número {numero_teste} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_teste} não pertence à sequência de Fibonacci.")
