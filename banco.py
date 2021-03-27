from contas import *
from ListaEncadeada import *
from PilhaEncadeada import *
from FilaEncadeada import *

class Banco:

    def __init__(self, nome, pilha, lista, fila):
        self._nome = nome
        self._contasP = pilha
        self._contasL = lista
        self._contasF = fila

#PROPRIEDADES:

    @property
    def contasP(self):
        return self._contasP

    @property
    def contasL(self):
        return self._contasL

    @property
    def contasF(self):
        return self._contasF

#MÉTODOS:

    def total_valor_contas(self):
        return self._contasL.soma

    def adiciona_valor_conta(self, valor, id):
        if self._contasL.vazio():
            raise ListaException("A lista está vazia!")

        p = self._contasL.inicio

        while p != None:
            if p.id == id:
                p.creditar(valor)
                self._contasL.soma = valor
                break
            else:
                p = p.prox
        else:
            raise ListaException("A conta informada não existe!")

    def adicionar_conta_P(self, nova_conta):
        self._contasP.adicionar(nova_conta)

    def adicionar_conta_L(self,nova_conta, posicao):
        self._contasL.adicionar(nova_conta, posicao)

    def adicionar_conta_F(self, nova_conta):
        self._contasF.adicionar(nova_conta)

    def remover_conta_P(self):
        self._contasP.remover()

    def remover_conta_L(self, posicao):
        self._contasL.remover(posicao)

    def remover_conta_F(self):
        self._contasF.remover()

    def busca_conta(self, id):
        return self._contasL.buscar(id)

    def ordena_contas(self):
        self._contasL.ordenar()

    def imprimir_contas(self):
        self._contasL.imprimir()

    def mostrar_tam_contasL(self):
        return self._contasL.tamanho()

    def mostrar_tam_contasP(self):
        return self._contasP.tamanho()

    def mostrar_tam_contasF(self):
        return self._contasF.tamanho()

    def __str__(self):
        return f"{self._contasP} \n{self._contasF} \n{self._contasL} "
