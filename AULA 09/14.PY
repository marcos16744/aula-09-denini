def numeros_primos(n):
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos
print(numeros_primos(10))  