"""
    Autores: Felipe Lopes e Maykon Siqueira.
    Desenvolvido no Python v3.6.5
"""
import re

# DICIONARIO DE TOKENS E LEXEMAS
regras = [
        ('token001', r'void'),              # PALAVRA RESERVADA void
        ('token002', r'int'),               # PALAVRA RESERVADA int
        ('token003', r'float'),             # PALAVRA RESERVADA float
        ('token004', r'char'),              # PALAVRA RESERVADA char
        ('token005', r'bool'),              # PALAVRA RESERVADA bool
        ('token006', r'if'),                # PALAVRA RESERVADA if
        ('token007', r'else'),              # PALAVRA RESERVADA else
        ('token008', r'for'),               # PALAVRA RESERVADA for
        ('token009', r'while'),             # PALAVRA RESERVADA while
        ('token010', r'do'),                # PALAVRA RESERVADA do
        ('token011', r'return'),            # PALAVRA RESERVADA return
        ('token012', r'break'),             # PALAVRA RESERVADA break
        ('token013', r'continue'),          # PALAVRA RESERVADA continue
        ('token014', r'goto'),              # PALAVRA RESERVADA goto
        ('token015', r'true'),              # PALAVRA RESERVADA true
        ('token016', r'false'),             # PALAVRA RESERVADA false
        ('token017', r'\+'),                # SIMBOLO +
        ('token018' , r'\-'),               # SIMBOLO -
        ('token019' , r'\*'),               # SIMBOLO *
        ('token020' , r'\/'),               # SIMBOLO /
        ('token021' , r'\%'),               # SIMBOLO %
        ('token022' , r'\?'),               # SIMBOLO ?
        ('token023' , r'\:'),               # SIMBOLO :
        ('token024' , r'\!'),               # SIMBOLO !
        ('token025' , r'\&'),               # SIMBOLO $
        ('token026' , r'\.'),               # SIMBOLO .
        ('token027' , r'->'),               # SIMBOLO ->
        ('token028' , r'<'),                # SIMBOLO <
        ('token029' , r'>'),                # SIMBOLO >
        ('token030' , r'=='),               # SIMBOLO ==
        ('token031' , r'!-'),               # SIMBOLO !-
        ('token032' , r'<='),               # SIMBOLO <=
        ('token033' , r'>='),               # SIMBOLO >=
        ('token034' , r'='),                # SIMBOLO =
        ('token035' , r'\+='),              # SIMBOLO +=
        ('token036' , r'\-='),              # SIMBOLO -=
        ('token037' , r'\*='),              # SIMBOLO *=
        ('token038' , r'\/='),              # SIMBOLO /=
        ('token039' , r'\%='),              # SIMBOLO %-
        ('token040' , r'\++'),              # SIMBOLO ++
        ('token041' , r'&&'),               # SIMBOLO &&
        ('token042' , r'\A\|\|'),           # SIMBOLO ||
        ('token043' , r','),                # SIMBOLO ,
        ('token044' , r';'),                # SIMBOLO ;
        ('token045' , r'\('),               # SOMBOLO (
        ('token046' , r'\)'),               # SIMBOLO )
        ('token047' , r'\]'),               # SIMBOLO ]
        ('token048' , r'\{'),               # SIMBOLO {
        ('token049' , r'\}'),               # SIMBOLO }
        ('token050' , r'endif'),            # PALAVRA RESERVADA endif
        ('token055' , r'print'),            # PALAVRA RESERVADA print
        ('token056' , r'printLn'),          # PALAVRA RESERVADA printLn
        ('token057' , r'var'),              # PALAVRA RESERVADA var
        ('token058' , r'real'),             # PALAVRA RESERVADA real
        ('token059' , r'scanf'),            # PALAVRA RESERVADA scanf
        ('token061' , r'scan'),             # PALAVRA RESERVADA scan
        ('token062' , r'main'),             # PALAVRA RESERVADA main
        ('token063' , r'end'),              # PALAVRA RESERVADA end
        ('token064' , r'"'),                # ASPAS DUPLAS
        ('token065', r'[a-zA-Z]\w*'),       # IDENTIFICADORES
        ('token066', r'\d(\d)*\.\d(\d)*'),  # FLOAT
        ('token067', r'\d(\d)*'),           # INT
        ('token098', r'\n'),                # NOVA LINHA
        ('token099', r'[ \t]+'),            # ESPACO OU TAB
        ('token100', r'.')                  # QUANDO NAO ENCONTRADO INCLUIR TUDO NESSE TOKEN
    ]

def ler_programa(arquivo):
    """
        :param arquivo: caminho do arquivo contendo o codigo
        :return: arquivo carregado na memoria
    """
    arq = open(arquivo, 'r')
    return arq

def analex(codigo):
    """
        :param codigo: recebe codigo que devera ser analisado pelo analex
    """
    # arquivo do log
    arquivo_log = open(r'log_lexico.txt', 'w')

    # remover comentarios multi-linhas /* */
    codigo = re.sub('\/\*(.|\s)*?\*\/', '', codigo)

    # remover comentarios de unica linha //
    codigo = re.sub('\/\/(.*)', '', codigo)

    # contador de linhas
    linha_atual = 0

    # monta uma string contendo todos os tokens da lista <regras>
    tokens_unificado = '|'.join('(?P<%s>%s)' % x for x in regras)
    str = f'[TOKEN_UNIFICADO] {tokens_unificado}'
    arquivo_log.write(str + '\n')

    # procurar elementos na lista de regras
    for m in re.finditer(tokens_unificado, codigo):
        # adiciona no log palavra sendo analisada atualmente
        str = f'[LOG] Analisando palavra:{m.group()}'
        arquivo_log.write(str + '\n')

        token = m.lastgroup     # pega a chave do ultimo grupo correspondente ou nao pega nenhum
        lexema = m.group(token) # pega o lexema da chave encontrada acima

        # imprime token mapeado
        str = f'[LOG] Token Mapeado:{token} Lexema:{lexema}'
        arquivo_log.write(str + '\n')

        # caso seja quebra de linha adicionamos o contador de linhas atuais
        if token == 'token098':
            linha_atual += 1
        # vamos ignorar os espacos e tabulacoes, pois o mesmo nao importa na linguagem sendo analisada
        elif token == 'token099':
            pass
        # caso nao exista correspondencia com os tokens analisados anteriormente (pelo re.find) exibimos erro lexico
        elif token == 'token100':
            str = f'[ERRO LEXICO] Elemento desconhecido: {lexema} na linha: {linha_atual}'
            arquivo_log.write(str + '\n')

    # fecha arquivo
    arquivo_log.close()

if __name__ == '__main__':
    # ler o codigo do arquivo
    programa = ler_programa('programas/1.d')

    # carregar o arquivo na memoria
    codigo = programa.read()

    # iniciar o analisador lexico
    analex(codigo)