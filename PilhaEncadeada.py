from contas import *

class PilhaException(Exception):

    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaEncadeada:

    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def adicionar(self, novaConta):
        novaConta.prox = self._topo
        self._topo = novaConta
        self._tamanho += 1

    def remover(self):
        if self.vazio():
            raise PilhaException("A pilha está vazia!")

        self._topo = self._topo.prox
        self._tamanho -= 1

    def vazio(self):
        return self._tamanho == 0

    def tamanho(self):
        return self._tamanho

    def mostrar_elemento(self):
        if self.vazio():
            raise PilhaException("A pilha está vazia!")

        return f"ID da Conta: {self._topo.id}"

    def __str__(self):
        retorno = "Pilha de contas: ["
        p = self._topo

        while p != None:
            retorno += f"ID: {p.id}"
            p = p.prox

            if p != None:
                retorno += ", "

        retorno += "]"

        return retorno

    def imprimir(self):
        print(self.__str__())