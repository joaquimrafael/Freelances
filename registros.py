#Programa para cadastro de civis por Joaquim Prieto

print('-' * 30)
print("*PROGRAMA DE CADASTRO*")
print('-' * 30)
n = int(input("Digite o número de usuários a cadastrar: "))
print()

#estrutura de repetição para cadastro de n usuários
while(n>0):
    #coleta de dados do usuário por teclado
    nome = input("Digite seu nome: ").strip().title()
    data = input("Data de nascimento(notação XX/XX/XXXX): ").strip()
    nacionalidade = input("Nacionalidade: ").strip().lower()
    registro = input("Registro Civil: ").strip()
    print()
    
    #cria a lista e adiciona os dados de maneira organizada
    lista = [nome, data, nacionalidade, registro]
    
    arquivo = open("registros.txt", "a")
    arquivo.write("-\n")
    
    #escreve as informações no console e no arquivo por iteração do for
    for i in lista:
      print(i)
      arquivo = open("registros.txt", "a")
      arquivo.write("{}\n".format(i))
    
    arquivo = open("registros.txt", "a")
    arquivo.write("\n")

    n -= 1
    print()

print()
print("FIM")
print('-' * 30)
