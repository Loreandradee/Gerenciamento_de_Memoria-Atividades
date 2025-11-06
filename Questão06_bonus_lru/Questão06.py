import sys

def algoritmo_fifo(referencias_paginas, quantidade_frames):
    """
    Implementa o algoritmo FIFO (First-In, First-Out) conforme a lógica
    da Questão 3 do documento (usando um ponteiro circular).
    """
    memoria = []              # Representa os quadros atuais na memória
    faltas_pagina = 0         # Contador de faltas de página
    posicao_atual = 0         # Indica qual quadro será substituído (ponteiro da fila)
    
    print("Executando FIFO")
    print("\n")
    
    for pagina in referencias_paginas:
        if pagina not in memoria:
            faltas_pagina += 1
            
            if len(memoria) < quantidade_frames:
                # Ainda há espaço, adicione a página
                memoria.append(pagina)
                print(f"Referência: {pagina} | Frames: {memoria} | Page Fault (livre)")
            else:
                # Memória cheia, substitua a página mais antiga (indicada por posicao_atual)
                pagina_removida = memoria[posicao_atual]
                memoria[posicao_atual] = pagina
                print(f"Referência: {pagina} | Frames: {memoria} | Page Fault (substituiu {pagina_removida})")
                
                # Atualiza o índice circularmente
                posicao_atual = (posicao_atual + 1) % quantidade_frames
        else:
            # Page Hit
            print(f"Referência: {pagina} | Frames: {memoria} | Page Hit")
            
    
    return faltas_pagina

def algoritmo_lru(referencias_paginas, quantidade_frames):
    """
    Implementa o algoritmo LRU (Least Recently Used) usando um
    dicionário para rastrear o "tempo" do último uso.
    """
    memoria = []              # Representa os quadros atuais na memória
    ultima_utilizacao = {}    # Guarda o "tempo" do último uso de cada página
    faltas_pagina = 0         # Contador de faltas de página
    tempo_logico = 0          # Relógio lógico, incrementa a cada referência

    print("\n")
    print("Executando LRU")
    print("\n")

    for pagina in referencias_paginas:
        tempo_logico += 1 # Avança o relógio
        
        if pagina not in memoria:
            faltas_pagina += 1
            
            if len(memoria) < quantidade_frames:
                # Ainda há espaço, adicione a página
                memoria.append(pagina)
                print(f"Referência: {pagina} | Frames: {memoria} | Page Fault (livre)")
            else:
                # Memória cheia, precisa substituir
                # Encontra a página menos recentemente usada (LRU)
                pagina_lru = None
                tempo_minimo = sys.maxsize
                
                # Itera *apenas* pelas páginas nos frames para achar a LRU
                for p_na_memoria in memoria:
                    if ultima_utilizacao[p_na_memoria] < tempo_minimo:
                        tempo_minimo = ultima_utilizacao[p_na_memoria]
                        pagina_lru = p_na_memoria
                
                # Remove a página LRU e adiciona a nova
                memoria.remove(pagina_lru)
                memoria.append(pagina)
                print(f"Referência: {pagina} | Frames: {memoria} | Page Fault (substituiu {pagina_lru})")
        
        else:
            # Page Hit
            print(f"Referência: {pagina} | Frames: {memoria} | Page Hit")
            
        # Atualiza o tempo de último uso da página atual
        ultima_utilizacao[pagina] = tempo_logico
            
    
    return faltas_pagina

# --- Função Principal para Comparação ---
if __name__ == "__main__":
    # Entrada EXATAMENTE IGUAL à da Questão 3 [cite: 457, 458]
    frames = 3
    referencias = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    total_referencias = len(referencias)

    print(f"Simulação com {frames} frames e sequência: {referencias}\n")

    # --- Execução e Resultados ---
    fifo_faults = algoritmo_fifo(referencias, frames)
    lru_faults = algoritmo_lru(referencias, frames)

    # --- 6.2. Comparação com FIFO ---
    print("\n")
    print(" 6.2. Comparação com FIFO: Page Faults e Taxa de Faltas")
    print("")
    
    # Dados do FIFO (Resultados da Questão 3 [cite: 551, 552])
    taxa_fifo = (fifo_faults / total_referencias) * 100
    print("Algoritmo FIFO:")
    print(f"Número de Faltas de Página: {fifo_faults}")
    print(f"Taxa de Faltas de Página:   {taxa_fifo:.2f}% ({fifo_faults}/{total_referencias})")
    
    # Dados do LRU (Resultados da Questão Bônus)
    taxa_lru = (lru_faults / total_referencias) * 100
    print("\nAlgoritmo LRU:")
    print(f"Número de Faltas de Página: {lru_faults}")
    print(f"Taxa de Faltas de Página:   {taxa_lru:.2f}% ({lru_faults}/{total_referencias})")
