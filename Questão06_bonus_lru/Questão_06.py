
#Simulação dos algoritmos de substituição de páginas: FIFO e LRU
#Autor: Caique daeski faria
#Descrição: Este programa compara o desempenho dos algoritmos
#FIFO e LRU
#mostrando o número e a taxa de faltas de página.

#Algoritmo FIFO (First-In, First-Out)
def algoritmo_fifo(referencias_paginas, quantidade_frames):
    memoria = []               #Representa os frames atuais na memória
    faltas_pagina = 0          #Contador de faltas de página
    posicao_atual = 0     
 #Indica qual frame será substituído

    for pagina in referencias_paginas:
        #Se a página não está na memória, ocorre uma falta
        if pagina not in memoria:
            faltas_pagina += 1

            #Se ainda há espaço, adiciona a página
            if len(memoria) < quantidade_frames:
                memoria.append(pagina)
            else:
                #Caso contrário, substitui a página mais antiga
                memoria[posicao_atual] = pagina
                #Atualiza o índice circularmente
                posicao_atual = (posicao_atual + 1) % quantidade_frames

    return faltas_pagina


#Algoritmo LRU (Least Recently Used)

def algoritmo_lru(referencias_paginas, quantidade_frames):
    memoria = []                #Representa os frames atuais na memória
    ultima_utilizacao = {}      #Guarda o "tempo" do último uso de cada página
    faltas_pagina = 0           #Contador de faltas de página
    tempo_atual = 0             #Contador de tempo
    
    for pagina in referencias_paginas:
        tempo_atual += 1  #A cada acesso, o tempo é incrementado

        if pagina in memoria:
            #Se a página já está na memória, apenas atualiza o tempo de uso
            ultima_utilizacao[pagina] = tempo_atual
        else:
            #Se a página não está na memória, ocorre uma falta
            faltas_pagina += 1

            #Se ainda há espaço disponível, insere a nova página
            if len(memoria) < quantidade_frames:
                memoria.append(pagina)
            else:
                #Encontra a página menos recentemente usada 
                pagina_antiga = min(ultima_utilizacao, key=ultima_utilizacao.get)
                #Substitui a página antiga pela nova
                memoria[memoria.index(pagina_antiga)] = pagina
                #Remove a antiga do dicionário de tempo
                del ultima_utilizacao[pagina_antiga]

            #Registra o tempo de uso da nova página
            ultima_utilizacao[pagina] = tempo_atual

    return faltas_pagina



#Função principal: leitura de dados e comparação dos algoritmos

if __name__ == "__main__":
    print("===== SIMULADOR DE SUBSTITUIÇÃO DE PÁGINAS =====\n")

    #Entrada de dados do usuário
    quantidade_frames = int(input("Informe o número de frames disponíveis: "))
    entrada = input("Digite a sequência de referências de páginas (ex: 7 0 1 2 0 3 0 4 2 3 0 3): ")

    #Converte a sequência em lista de inteiros
    referencias_paginas = list(map(int, entrada.strip().split()))

    #Executa os algoritmos
    faltas_fifo = algoritmo_fifo(referencias_paginas, quantidade_frames)
    faltas_lru = algoritmo_lru(referencias_paginas, quantidade_frames)

    #Calcula as taxas de falta de página
    taxa_fifo = faltas_fifo / len(referencias_paginas)
    taxa_lru = faltas_lru / len(referencias_paginas)

    #Exibe os resultados de forma organizada
    print("\n===== RESULTADOS =====")
    print(f"Total de referências de página: {len(referencias_paginas)}")
    print(f"Frames disponíveis: {quantidade_frames}")
    print(f"Faltas de página (FIFO): {faltas_fifo}  →  {taxa_fifo:.2%} de taxa de falta")
    print(f"Faltas de página (LRU):  {faltas_lru}  →  {taxa_lru:.2%} de taxa de falta")

    #Análise comparativa dos resultados
    print("\n===== ANÁLISE COMPARATIVA =====")
    if faltas_lru < faltas_fifo:
        print("O algoritmo **LRU** apresentou melhor desempenho, com menos faltas de página.")
    elif faltas_lru > faltas_fifo:
        print("O algoritmo **FIFO** teve menos faltas de página neste caso específico.")
    else:
        print("Ambos os algoritmos tiveram o mesmo número de faltas de página.")

    #Observações gerais
    print("\n===== CONCLUSÃO =====")
    print("- O algoritmo FIFO é mais simples, mas pode substituir páginas ainda necessárias (anomalia de Belady).")
    print("- O algoritmo LRU é mais eficiente na maioria dos casos, pois mantém em memória as páginas usadas recentemente.")
    print("- Em cargas de trabalho reais, o LRU costuma ter melhor desempenho geral.\n")