class Conta:

    def __init__ (self, id, cpf, saldo):
        self._id = id
        self._cpf = cpf
        self._saldo = saldo
        self._prox = None

#GET

    @property
    def id (self):
        return self._id

    @property
    def cpf (self):
        return self._cpf

    @property
    def saldo (self):
        return self._saldo

    @property
    def prox (self):
        return self._prox

#SET

    @id.setter
    def id (self, novo_id):
        self._id = novo_id

    @cpf.setter
    def cpf (self, novo_cpf):
        self._cpf = novo_cpf

    @saldo.setter
    def saldo (self, novo_saldo):
        self._saldo = novo_saldo

    @prox.setter
    def prox (self, novo_prox):
        self._prox = novo_prox


#MÉTODOS

    def creditar (self, valor_credito):
        self._saldo = self._saldo + valor_credito

    def debitar (self, valor_debito):
        if self._saldo >= valor_debito:
            self._saldo = self._saldo - valor_debito
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"ID: {self._id}, SALDO: {self._saldo} R$"



