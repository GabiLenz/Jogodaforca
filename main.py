from funcoes import limparTela, esperarSegundos, soma, lerString
limparTela()
print("Jogo da Forca! ")
esperarSegundos(3)
limparTela()
print ("Nome do Desafiante ")
nome = lerString ("Nome: ")
arquivo = open("dados.forca", "a")
arquivo.write(nome + "\n")
arquivo.close()
print("Nome Salvo")
esperarSegundos(1)
limparTela()
print ("Nome do Competidor ")
nome = lerString ("Nome: ")
arquivo = open("dados.forca", "a")
arquivo.write(nome + "\n")
arquivo.close()
print("Nome Salvo")
esperarSegundos(1)
limparTela()
print("Desafiante Informe a Palavra ")
palavra = lerString ("Palavra: ")
arquivo = open("dados.forca", "a")
arquivo.write(palavra + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 1 ")
dica1 = lerString ("Dica 1: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica1 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 2 ")
dica2 = lerString ("Dica 2: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica2 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 3 ")
dica3 = lerString ("Dica 3: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica3 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
while True:
   print("Quantidade de letras ↆ ")
   print(" _ "*len(palavra))
   print("(0)Jogar")
   print("(1)Solicitar Dica")
   print("(2)Sair do Jogo")
   opcao=input()
   if opcao == "2":
    break
   elif opcao == "1":
    limparTela()
    print(dica1)
   elif opcao == "0":
     letra=input("Digite a letra: ")
     if letra in palavra:
       


    



