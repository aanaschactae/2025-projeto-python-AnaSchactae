'''
Funções usadas no projeto
2025. 07. 04
Ana Vitória Schactae Brandão
'''

# OBJETIVO: Criar um arquivo de funções que serão utilizadas no projeto final - Ad Verbum

# CONSTANTES
LIN = int(25) #Tamanho da linha
CAR1 = '★-'    # Caracteres utilizados
CAR2 = '-★'
TAM = int(50) # Tamanho da tela
MAR = int(2)  # Tamanho da Margem

# FUNÇÃO
# Função para desenhar uma linha
def drawLine():
    print(f'{CAR1}'*LIN) 

# Função para mostrar uma mensagem centralizada
def msgCenter(msg):
    print(f'{CAR1} {msg:^{(TAM-MAR)-MAR-MAR}} {CAR2}') # Mostra na tela o valor do parametro msg Centralizado entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar uma Msg a Esquerda
def msgLeft(msg):
    print(f'{CAR1} {msg:<{TAM-MAR-MAR}} {CAR2}') # Mostra na tela o valor do parametro msg a esquerda entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar Cabeçalho
def mostraCabecalho(MSGS):
    drawLine()            # Chama a função que mostra a linha
    for msg in MSGS:        # Itera sobre a lista MSGS
        msgCenter(msg)      # Chama a função que mostra a mensagem centralizada 
    drawLine()            # Chama a função que mostra a linha

# Função para mostrar Instruções
def mostraInst(MSGS):   
    drawLine()            # Chama a função que mostra a linha
    for msg in MSGS:        # Itera sobre a lista MSGS
        msgLeft(msg)        # Chama a função que mostra a mensagem a esquerda 
    drawLine()            # Chama a função que mostra a linha


# Função para obter a entrada do usuário
def getValue(msg):
    resp = input(f'{CAR1} {msg}: ').strip()
    return resp

# Função para Validar as Entradas
def validaValue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
        MSGS = [f'{resp} não é uma opção válida!', 
                f'Escolha entre {opcoes}']
        return False

# Função para perguntar se o jogador quer jogar novamente
def playAgain():
    opcoes = ['Sim', 'Não']
    mostraCabecalho(['Deseja jogar novamente?', 'Sim', 'Não'])
    resp = getValue('Escolha uma opção')
    return resp == '1'

drawLine()
playAgain()