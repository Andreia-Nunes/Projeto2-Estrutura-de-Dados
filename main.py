from banco import *
from contas import *
from FilaEncadeada import *
from ListaEncadeada import *
from PilhaEncadeada import *

#Criando objetos conta:
contaA = Conta(0, "000.000.000-00", 10000)
contaB = Conta(1, "111.111.111-11", 15000)
contaC = Conta(2, "222.222.222-22", 20000)
contaD = Conta(3, "333.333.333-33", 25000)
contaE = Conta(4, "444.444.444-44", 30000)

contaF = Conta(5, "555.555.555-55", 35000)
contaG = Conta(6, "666.666.666-66", 40000)
contaH = Conta(7, "777.777.777-77", 45000)
contaI = Conta(8, "888.888.888-88", 50000)
contaJ = Conta(9, "999.999.999-99", 55000)

contaK = Conta(10, "101.101.101.10", 60000)
contaL = Conta(11, "102.102.102.10", 65000)
contaM = Conta(12, "103.103.103-10", 70000)
contaN = Conta(13, "104.104.104-10", 75000)
contaO = Conta(14, "105.105.105-10", 80000)

#Criando objetos pilha, lista e fila:
pilhaContas = PilhaEncadeada()
listaContas = ListaEncadeada()
filaContas = FilaEncadeada()

#Adicionando contas à pilha:
pilhaContas.adicionar(contaA)
pilhaContas.adicionar(contaB)
pilhaContas.adicionar(contaC)
pilhaContas.adicionar(contaD)
pilhaContas.adicionar(contaE)

#Adicionando contas à lista:
listaContas.adicionar(contaG, 0)
listaContas.adicionar(contaI, 1)
listaContas.adicionar(contaF, 2)
listaContas.adicionar(contaJ, 3)
listaContas.adicionar(contaH, 4)

#Adicionando contas à fila
filaContas.adicionar(contaK)
filaContas.adicionar(contaL)
filaContas.adicionar(contaM)
filaContas.adicionar(contaN)
filaContas.adicionar(contaO)

#Criando o objeto banco:
banco = Banco("Banco do Brasil", pilhaContas, listaContas, filaContas)

flag = "S"
opcao: int

#Criando o menu:
while flag == "S":
    print("\n------------------------- MENU -------------------------")
    print("\nOpções:")
    print("\n1- Consultar o valor total das contas na lista")
    print("2- Creditar em conta da lista")
    print("3- Adicionar conta à pilha")
    print("4- Adicionar conta à lista")
    print("5- Adicionar conta à fila")
    print("6- Remover conta da pilha")
    print("7- Remover conta da lista")
    print("8- Remover conta da fila")
    print("9- Buscar conta na lista")
    print("10- Ordenar contas da lista")
    print("11- Imprimir contas da lista")
    print("12- Mostrar o tamanho da lista de contas")
    print("13- Mostrar o tamanho da pilha de contas")
    print("14- Mostrar o tamanho da fila de contas")
    print("15- Sair")

    opcao = int(input(f"\nInsira a opção desejada: "))
    print()

    if opcao == 1:
        print(f"Total das contas na lista: {banco.total_valor_contas():.2f} R$")

    elif opcao == 2:
        valor_creditado = float(input("Valor a ser creditado: "))
        id_conta = int(input("ID da conta: "))

        try:
            banco.adiciona_valor_conta(valor_creditado, id_conta)
            print("\nValor creditado com sucesso!")

            p = banco.contasL.inicio

            while p != None:
                if p.id == id_conta:
                    print(f"\nSaldo: {p.saldo} R$")
                    break
                else:
                    p = p.prox

        except ListaException as le:
            print(le)
            print("\nO valor não foi creditado!")

    elif opcao == 3:
        id_nova_conta = int(input("Informe o ID da conta: "))
        cpf_nova_conta = input("Informe o CPF: ")
        saldo_nova_conta = float(input("Informe o saldo: "))

        nova_conta = Conta(id_nova_conta, cpf_nova_conta, saldo_nova_conta)

        banco.adicionar_conta_P(nova_conta)

        print("\nConta adicionada com sucesso!")
        print(f"\n{banco.contasP}")

    elif opcao == 4:
        id_nova_conta = int(input("Informe o ID da conta: "))
        cpf_nova_conta = input("Informe o CPF: ")
        saldo_nova_conta = float(input("Informe o saldo: "))

        nova_conta = Conta(id_nova_conta, cpf_nova_conta, saldo_nova_conta)

        pos = int(input("Informe a posição desejada para inserção: "))

        try:
            banco.adicionar_conta_L(nova_conta, pos)
            print("\nConta adicionada com sucesso!")
            print(f"\n{banco.contasL}")
        except ListaException as le:
            print(le)
            print("\nA conta não foi adicionada!")

    elif opcao == 5:
        id_nova_conta = int(input("Informe o ID da conta: "))
        cpf_nova_conta = input("Informe o CPF: ")
        saldo_nova_conta = float(input("Informe o saldo: "))

        nova_conta = Conta(id_nova_conta, cpf_nova_conta, saldo_nova_conta)

        banco.adicionar_conta_F(nova_conta)
        print("\nConta adicionada com sucesso!")
        print(f"\n{banco.contasF}")

    elif opcao == 6:
        try:
            banco.remover_conta_P()
            print("Conta removida com sucesso!")
            print(f"\n{banco.contasP}")
        except PilhaException as pe:
            print(f"{pe}")

    elif opcao == 7:
        pos = int(input("Informe a posição desejada para remoção: "))

        try:
            banco.remover_conta_L(pos)
            print("\nConta removida com sucesso!")
            print(f"\n{banco.contasL}")
        except ListaException as le:
            print(f"\n{le}")

    elif opcao == 8:
        try:
            banco.remover_conta_F()
            print("Conta removida com sucesso!")
            print(f"\n{banco.contasF}")
        except FilaException as fe:
            print(f"{fe}")

    elif opcao == 9:
        id = int(input("Insira o ID da conta: "))

        try:
            print(f"{banco.busca_conta(id)}")
            print(banco.contasL)
        except ListaException as le:
            print(f"{le}")

    elif opcao == 10:
        banco.ordena_contas()
        print("Lista ordenada com sucesso!")
        print(f"\n{banco.contasL}")

    elif opcao == 11:
        banco.imprimir_contas()

    elif opcao == 12:
        print(f"Tamanho da lista de contas: {banco.mostrar_tam_contasL()} elementos.")
        print(f"\n{banco.contasL}")

    elif opcao == 13:
        print(f"Tamanho da pilha de contas: {banco.mostrar_tam_contasP()} elementos.")
        print(f"\n{banco.contasP}")

    elif opcao == 14:
        print(f"Tamanho da fila de contas: {banco.mostrar_tam_contasF()} elementos.")
        print(f"\n{banco.contasF}")

    else:
        print("SESSÃO ENCERRADA!")
        break

    flag = input("\nDeseja realizar outra operação? (S/N) ").upper()

else:
    print("SESSÃO ENCERRADA!")










