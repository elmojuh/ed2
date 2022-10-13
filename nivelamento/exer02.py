
class No:
    def __init__(self, val):
        self.valor = val
        self.proximo = None


class ListaEncadeada:
    def __init__(self, head=None):
        self.head = None

    def add(self, val):
        novoNo = No(val)

        # Se lista encadeada vazia:
        if self.head is None:
            self.head = novoNo
            return

        # Percorrendo a lista até o fim
        aux = self.head
        while aux.proximo:
            aux = aux.proximo
        aux.proximo = novoNo

    def printLista(self):
        if self.head is None:
            return ""

        no = self.head
        while no:
            print(no.valor, end=" | ")
            no = no.proximo

    def ordernarLista(self):
        ultimo = []
        while self.head:
            ultimo.append(self.head.valor)
            self.head = self.head.proximo

        ultimo.sort()
        aux = ListaEncadeada()
        for num in ultimo:
            aux.add(num)
        return aux


if __name__ == '__main__':
    # teste com lista dada
    lista = ListaEncadeada()
    lista.add(1)
    lista.add(5)
    lista.add(4)
    lista.add(3)
    lista.add(2)
    lista.add(6)
    lista.add(7)
    print('Vagas dada: ')
    lista.printLista()
    print()
    listaOrdenada = lista.ordernarLista()
    print('Vagas ordenada: ')
    listaOrdenada.printLista()