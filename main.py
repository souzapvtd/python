import random as rd



#Começo/Inicio
print("-------------------------------")
print("\nBem vindo ao jogo da prestigitação!\n")
print("-------------------------------")

#Variáveis
n_secreto = (rd.rangrange(1,101))
n_tentativas = 5
rodada = 1

for rodada in range (1,n_tentativas +1):
    print(f"Tentativa {rodada} de {n_tentativas}")
    print(f"Número de tentativas: {n_tentativas}")
    entrada = int(input("Digite um número entre 1 e 100:"))
    acertou = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("O valor digitado não é permitido!")
        continue 


#Verificação de acerto/erro
    print(f"\nVocê digitou o número: {entrada}")

    if(acertou):
            print("Parabéns, você acertou o número secreto")
            break
    else:
        if(entrada_maior):
                    print("Você errou! O número digitado foi maior que o secreto")
        if(entrada_menor):
                    print("Você errou! O número digitado foi menor que o secreto")
    rodada = rodada + 1

print("\nFim de jogo")