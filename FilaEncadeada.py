from contas import *

class FilaException(Exception):

    def __init__(self, mensagem):
        super().__init__(mensagem)


class FilaEncadeada:

    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    def adicionar(self, novaConta):
        auxiliar = self._inicio

        if auxiliar == None:
            self._inicio = novaConta
        else:
            while auxiliar.prox != None:
                auxiliar = auxiliar.prox

            auxiliar.prox = novaConta

        self._tamanho += 1

    def remover(self):
        if self.vazia():
            raise FilaException("A fila está vazia!")

        self._inicio = self._inicio.prox
        self._tamanho -= 1

    def vazia(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    def mostrar_elemento(self):
        if self.vazia():
            raise FilaException("A pilha está vazia!")

        return f"ID da Conta: {self._inicio.id}"

    def __str__(self):
        saida = "Fila de contas: ["
        p = self._inicio

        while p != None:
            saida += f"ID: {p.id}"
            p = p.prox

            if p != None:
                saida += ", "

        saida += "]"
        return saida

    def imprimir(self):
        print(self.__str__())
