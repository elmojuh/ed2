# Supondo que a String é a frase "Frase deve ser invertida palavra a palavra"
# Em uma pilha onde o ultimo elemento inserido será o primeiro a ser retirado.
# Inseri-se letra a letra e depois se retira novamente da pilha. No filtro da frase, a cada espaço( ) encontrado,
# a função se inicia, e constroi a pilha e retira os elementos. A pilha terá seus elementos
# reestruturados em ordem inversa.
from collections import deque

string = 'Frase deve ser invertida'


def reverterFrase(frase):
    #cria pilha
    pilha = deque()

    #Adiciona letra a letra da frase na nova pilha
    for letra in frase:
        pilha.append(letra)

    #criando nova  string para receber retorno da pilha
    fraseInvertida = ''

    #remove elementos da pilha para serem inseridos na string
    while pilha:
        fraseInvertida = fraseInvertida + pilha.pop()

    return fraseInvertida


def reverterRecursivo(string):
    if len(string) == 0:
        return string
    else:
        #reinicia funcao a cada letra
        return reverterRecursivo(string[1:]) + string[0]


print("\nA frase original é: ", end="\n")
print(string)
print("\nReverter modo fávil: ", end="\n")
print(reverterFrase(string))
print("\nReverter recursivo: ", end="\n")
print(reverterRecursivo(string))