print("-------------------------------")
print("\nBem-vindo ao Jogo de Identificação de Números!\n")
print("===============================")


numero_secreto = 42
n_tentativas = 5  
rodada = 1 

for rodada in range(1, n_tentativas + 1):
    print(f"Tentativa {rodada} de {n_tentativas}")
    
   
    numero_usuario = int(input("Digite um número entre 1 e 100: "))
    

    if numero_usuario == numero_secreto:
        print("\n Parabéns! Você identificou o número secreto!")
        break 
    else:
        if numero_usuario > numero_secreto:
            print("Você errou! O número digitado é maior que o número secreto.")
        elif numero_usuario < numero_secreto:
            print("Você errou! O número digitado é menor que o número secreto.")
    
    rodada += 1  


if rodada > n_tentativas:
    print("\nVocê não conseguiu identificar o número secreto. Fim de jogo.")

print("\nFim de jogo!")