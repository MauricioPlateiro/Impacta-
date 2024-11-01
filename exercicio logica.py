n1 = 10
n2 = 5
print("Início")
print(f"n1 = {n1}")
print(f"n2 = {n2}")
print("Primeira condição é n1 % n2 > 1")
if n1 % n2 > 1:
    print(f"{n1 % n2} > 1 é verdadeiro, então verifica a segunda condição: 3 + 5 / n2 > 4")
    if 3 + 5 / n2 > 4:
        print(f"{3 + 5 / n2} > 4 é verdadeiro então mantém n1 com o valor atual")
        pass # não faz nada
    else:
        print(f"{3 + 5 / n2} > 4 é falso então atribui n2 = n1 + 5 = {n1 + 5}")
        n2 = n1 + 5
else:
    print(f"{n1 % n2} > 1 é falso na primeira condição então verifica a segunda condição n1 // n2 > 1")
    if n1 // n2 > 1:
        print(f"{n1 // n2} > 1 é verdadeiro então atribui n2 = n1 + 5 = {n1 + 5}")
        n2 = n1 + 5
    else:
        print(f"{n1 // n2} > 1 é falso então atribui n1 = n2 + 5 = {n2 + 5}")
        n1 = n2 + 5

print("Terceira condição é se 2 + n1 / 2 * 3 >= 18")
if 2 + n1 / 2 * 3 >= 18:
    #Obs.: a função round() arredonda o valor para o inteiro mais próximo, fiz isso apenas para formatar a exibição na tela
    print(f"{round(2 + n1 / 2 * 3)} >= 18 é verdadeiro então atribui n1 = n1 % n2 = {n1 % n2}")
    n1 = n1 % n2
else:
    print(f"{round(2 + n1 / 2 * 3)} >= 18 é falso então atribui n2 = n2 % n1 = {n2 % n1 }")
    n2 = n2 % n1

print(f"n1 = {n1}")
print(f"n2 = {n2}")
print("Soma final de n1+n2 = ", n1 + n2)
print("Fim")