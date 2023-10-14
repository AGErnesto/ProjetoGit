# Mensagem de boas vindas
print("Bem vindo à Textburguer!")
print("Vamos definir o estoque que temos agora")
pao = int(input ("Quantos pães você tem hoje?\n"))
#queijo = input ("Quantas fatias de queijo você tem hoje?\n")
carne = int(input ("Quantos hamburgueres você tem hoje?\n"))
#Bacon = input ("Quantas fatias de bacon você possui hoje?\n")
#picles = input ("Quantas fatias de picles você possui hoje? \n")

resposta = input ("Vamos começar a preparar os lanches?\n")
  
if resposta == "Sim":
    pedido = input ("Qual será seu lanche?\n 1 - Cheeseburger\n 2 - Bacon\n")
    adicionais = input ("Simples ou duplo?\n")
    print(f"Beleza, seu pedido vai ser {pedido}, {adicionais}")
    
    if pedido == "Cheeseburguer":
        pao -= 1
        #queijo -= 1
        #picles -= 1
    
    if pedido == "Bacon":
        pao -= 1
        #queijo -= 1
        #bacon -= 1
        #picles -= 1
    
    if adicionais == "Simples":
         carne -= 1
    else:
        carne -= 2
    

        
    print ("Seu pedido está pronto\n")
    print ("Sobraram os seguinte ingredientes\n")
    print (f"{pao} pão")
    print (f"{carne} carne")
else:
        print ("Okay então, tchau")
