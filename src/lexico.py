"""
    Autor: Felipe Lopes
    Autor: Maykon Siqueira
    Objetivo: Desenvolver analisador lexico para discplina compiladores
"""
import re
import sys


# carregar globalmente dict de tokens
tokens = [
        (r'[void]', 'token001'),
        (r'[int]', 'token002'),
        (r'[float]', 'token003'),
        (r'[char]', 'token004'),
        (r'[bool]', 'token005'),
        (r'[if]', 'token006'),
        (r'[else]', 'token007'),
        (r'[for]', 'token008'),
        (r'[while]', 'token009'),
        (r'[do]', 'token010'),
        (r'[return]', 'token011'),
        (r'[break]', 'token012'),
        (r'[continue]', 'token013'),
        (r'[goto]', 'token014'),
        (r'[true]', 'token015'),
        (r'[false]', 'token016'),
        (r'[+]', 'token017'),
        (r'[-]', 'token018'),
        (r'[*]', 'token019'),
        (r'[/]', 'token020'),
        (r'[%]', 'token021'),
        (r'[?]', 'token022'),
        (r'[:]', 'token023'),
        (r'[!]', 'token024'),
        (r'[&]', 'token025'),
        (r'[.]', 'token026'),
        (r'[->]', 'token027'),
        (r'[<]', 'token028'),
        (r'[>]', 'token029'),
        (r'[==]', 'token030'),
        (r'[!-]', 'token031'),
        (r'[<=]', 'token032'),
        (r'[>=]', 'token033'),
        (r'[=]', 'token034'),
        (r'[+=]', 'token035'),
        (r'[-=]', 'token036'),
        (r'[*=]', 'token037'),
        (r'[/=]', 'token038'),
        (r'[%=]', 'token039'),
        (r'[++]', 'token040'),
        (r'[&&]', 'token041'),
        (r'[||]', 'token042'),
        (r'[,]', 'token043'),
        (r'[;]', 'token044'),
        (r'[(]', 'token045'),
        (r'[)]', 'token046'),
        (r'[[]', 'token047'),
        (r'[{]', 'token048'),
        (r'[}]', 'token049'),
        (r'[endif]', 'token050')
    ]

def ler_programa(arquivo):
    arq = open(arquivo, 'r')
    return arq

def analisador():
    print("Inicializando analisador")

    # percorre lista de tokens para comparacao com o codigo do input
    for regra, token in tokens:
        # imprimir teste
        print("Regra:{} Token:{}".format(re.compile(regra), token))


if __name__ == '__main__':

    # ler o codigo do arquivo
    programa = ler_programa('programas/1.d')

    # carregar o codigo para memoria
    codigo = programa.read()

    # inicializar o analisador lexico
    analisador(codigo)