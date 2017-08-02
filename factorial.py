def fact(n):

    if n<= 1:
        return 1
    else:
        return n * fact(n - 1)

x = input("Número para calcular o fatorial:")
print("O fatorial de",x,"é" ,fact(int(x)), ".")
input()

