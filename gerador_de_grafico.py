import matplotlib.pyplot as plt
import numpy as np

def escolhe():
    doc = input('Escolha o arquivo a ser aberto:')
    arquivo = open(doc)
    return arquivo

arquivo = escolhe()

# Lista que le o arquivo da matriz, e armazena em uma lista outras listas cada uma com uma linha da matriz.
with arquivo as matriz:
    meses = [list(map(int,linha.split()))for linha in matriz]

# Lista com nome dos mesês
nome_mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sete', 'out', 'nov', 'dez']

# Data (por enquanto vazio :p)
lista_apropriado = [] 
lista_colheita = []
chuvas_mes=[]

# i e dias percorrem respectivamente a lista com nome dos mesês e a lista com uma linha da matriz, e associa o nome do mês com essa linha.
for i, dias in zip(nome_mes,meses):
    apropriado = 0
    colheita = 0
    # percorre os dias(-2 para a verificação de dia apropriado não sair do limite de dias)
    for n in range(len(dias) - 2):
        
        # Se n verificar uma casa da lista de dias com 1 e os proximos dois dias forem 0 ele soma 1 para dia apropriado 
        if dias[n] == 1 and dias[n+1] == 0 and dias[n+2] == 0:
            apropriado +=1
    for n in range(len(dias)-3):
        if dias[n]==1 and dias[n+1] == 0 and dias[n+2] == 0 and dias[n+3] == 0:
            colheita += 1 

            
    # Separa em uma lista os dias apropriados para usar depois para associar com o mês respectivamente
    lista_apropriado.append(apropriado)
    lista_colheita.append(colheita)
    # Se n em dias (que são 30) for igual a 1 ele vai somar +1 para a variavel choveu
    choveu = sum(n == 1 for n in dias)
    # Separa em uma lista quantos dias choveram para usar depois para associar com o mês respectivamente
    chuvas_mes.append(choveu)
    # Só printar o mês, # é a quantidade de dias apropriados para chuva, e oque esta () é quantos dias de fato choveram no mês
    print('{}:{} ({})'.format(i,'#'*apropriado,choveu)) 

# Prova para associar dias apropriados com quantos choveram para verificar se esta td certinho :D  
print('Leve em conta que a posição da lista se associa com o mês')
print('Lista com dias apropriados para plantar:{}\nLista com quantidade de dias bons para colheita:{}\nQuantidade dias de dias de chuva:{}'.format(lista_apropriado, lista_colheita,chuvas_mes))
input('Aperte enter para gerar o gráfico')
# Cria uma sequencia com valor 12 para j.
j = len(nome_mes)

# Criando uma figura e um eixo.
fig, ax = plt.subplots()

# Permite criar uma sequência de valores com base nos parâmetros fornecidos.
index = np.arange(j)

# Definir a largura e a opacidade da barra.
largura_barra = 0.3
opacidade = 0.8

# Cria as barras que se relacionam com a qtd de chuvas e a com a qtd de dias apropriados para plantio
barra_chuvas = ax.bar(index, chuvas_mes, largura_barra, alpha=opacidade, color='b', label='Qtd de Dias que Choveram')
barra_apropriados = ax.bar(index + largura_barra, lista_apropriado, largura_barra, alpha=opacidade, color='r', label='Qtd de Dias Apropriados para Plantio')
barra_colheita = ax.bar(index - largura_barra, lista_colheita, largura_barra, alpha=opacidade, color='g', label='Qtd de Dias bons para colher')

# legendas e dados
ax.set_xlabel('Mesês')
ax.set_ylabel('Dias')
ax.set_title('Qtd de Dias de Chuva e Qtd de Dias Apropriados para Plantio')
ax.set_xticks(index + largura_barra / 2)
ax.set_xticklabels(nome_mes)
ax.set_ylim(0,30)
ax.legend()

# Mostra o valor no grafico para melhor entendimento
ax.bar_label(barra_chuvas, padding=3, color='blue', fontweight='regular')
ax.bar_label(barra_apropriados, padding=3, color='red', fontweight='regular')
ax.bar_label(barra_colheita, padding=3, color='green', fontweight='regular')

# Plota o gráfico.
plt.show()
quit(1)