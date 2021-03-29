from contas import *

class ListaException(Exception):

    def __init__(self, mensagem):
        super().__init__(mensagem)


class ListaEncadeada:

    def __init__(self):
        self._inicio = None
        self._tamanho = 0
        self._soma = 0

    #--------------------------- PROPRIEDADES ---------------------------

    @property
    def inicio(self):
        return self._inicio

    @property
    def soma(self):
        return self._soma

    @soma.setter
    def soma(self, valor):
        self._soma += valor

    #--------------------------- MÉTODOS ---------------------------

    def adicionar(self, novaConta, pos):
        if self.vazio() or pos == 0:
            novaConta.prox = self._inicio
            self._inicio = novaConta
        elif pos == self._tamanho:
            p = self._inicio

            for cont in range(0, pos - 1):
                p = p.prox

            p.prox = novaConta
        else:
            p = self._inicio
            q = None

            for cont in range(0, pos):
                if p.prox != None:
                    q = p
                    p = p.prox
                else:
                    raise ListaException("A posição informada não existe!")

            novaConta.prox = p
            q.prox = novaConta

        self._tamanho += 1
        self._soma += novaConta.saldo

    def remover(self, pos):
        if self.vazio():
            raise ListaException("A lista está vazia!")
        else:
            if pos == 0:
                self._inicio = self._inicio.prox
                self._tamanho -= 1
            else:
                p = self._inicio
                q = None

                for cont in range(0, pos):
                    if p.prox != None:
                        q = p
                        p = p.prox
                    else:
                        raise ListaException("A posição informada não existe!")

                q.prox = p.prox
                self._tamanho -= 1
                self._soma -= p.saldo

    def vazio(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    def mostrar_Elemento(self, pos):
        if self.vazio():
            raise ListaException("A lista está vazia!")

        p = self._inicio

        for cont in range(0, pos):
            if p.prox != None:
                p = p.prox
            else:
                raise ListaException("A posição informada não existe!")

        return f"Conta na posição {pos}: ID {p.id}"

    def ordenar(self):
        vetor_ID = []
        p = self._inicio

        if p == None:
            raise ListaException("A lista não contém elementos!")
        else:
            while p != None:
                vetor_ID.append(p.id)
                p = p.prox

        vetor_ID.sort()

        vetor_Contas = []

        for i in range(0, len(vetor_ID)):
            p = self._inicio

            while p != None:
                if vetor_ID[i] == p.id:
                    vetor_Contas.append(p)
                    break
                else:
                    p = p.prox

        self._inicio = vetor_Contas[0]

        for i in range(0, len(vetor_Contas) - 1):
            vetor_Contas[i].prox = vetor_Contas[i+1]

        vetor_Contas[len(vetor_Contas) - 1].prox = None

    def buscar(self, id):
        if self.vazio():
            raise ListaException("A lista está vazia!")

        p = self._inicio

        for cont in range(0, self._tamanho):
            if p.id == id:
                return f"Posição da conta com ID {id} na lista: {cont}"
            else:
                if p.prox != None:
                    p = p.prox
                else:
                    raise ListaException("Não existe conta com o ID informado!")

    def __str__(self):
        retorno = "Lista de contas: ["

        p = self._inicio

        while p != None:
            retorno += f"ID: {p.id}"
            p = p.prox

            if p != None:
                retorno += ", "

        retorno += "]"

        return retorno

    def imprimir(self):
        retorno = "Lista de contas: ["

        p = self._inicio

        while p != None:
            retorno += f"ID: {p.id} CPF: {p.cpf}"
            p = p.prox

            if p != None:
                retorno += ", "

        retorno += "]"

        print(retorno)
