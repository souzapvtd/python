print("-------------------------------")
print("\nBem-vindo ao Jogo de Identificação de Números!\n")
print("-------------------------------")


numero_secreto = 42
n_tentativas = 5  
tentativas_restantes = n_tentativas 

while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}")
    
  
    numero_usuario = int(input("Digite um número entre 1 e 100: "))
    
 
    if numero_usuario == numero_secreto:
        print("\n Parabéns! Você identificou o número secreto! ")
        break 
    else:
        if numero_usuario > numero_secreto:
            print("Você errou! O número digitado é maior que o número secreto.")
        elif numero_usuario < numero_secreto:
            print("Você errou! O número digitado é menor que o número secreto.")
    
    tentativas_restantes -= 1 


if tentativas_restantes == 0:
    print("\nVocê não conseguiu identificar o número secreto. Fim de jogo.")

print("\nFim de jogo!")