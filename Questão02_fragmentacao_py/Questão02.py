# --- Estrutura da Memória --- 
# Cada partição é um dicionário com:
# 'tamanho': quantidade de unidades
# 'processo': None se estiver livre, ou nome do processo se estiver ocupada

particoes = [
    {"tamanho": 100, "processo": None},
    {"tamanho": 150, "processo": None},
    {"tamanho": 200, "processo": None},
    {"tamanho": 250, "processo": None},
    {"tamanho": 300, "processo": None},
]

# Lista que armazena a fragmentação interna acumulada
frag_total = []

# --- Função para alocar processos ---
def alocar(nome, tamanho): # Aloca um processo usando algoritmo First-Fit e Calcula e exibe a fragmentação interna.
    for i, particao in enumerate(particoes):
        if particao["processo"] is None and particao["tamanho"] >= tamanho:
            particao["processo"] = nome
            frag_interna = particao["tamanho"] - tamanho 
            frag_total.append(frag_interna)
            print(f"Processo {nome} alocado na partição {i+1} "
                  f"(Fragmentação interna: {frag_interna})")
            return
    print(f"Falha ao alocar {nome}: nenhuma partição disponível suporta o processo.")

# --- Função para liberar processos (simplificada) ---

def liberar(nome): # Libera a partição ocupada pelo processo.
    for i, particao in enumerate(particoes):
        if particao["processo"] == nome:
            particao["processo"] = None
            print(f"Processo {nome} liberado da partição {i+1}.")
            return
    print(f"Processo {nome} não encontrado.")

# --- Função para exibir estado da memória ---

def mostrar(): # Mostra todas as partições, seus tamanhos e processos alocados.
    print("\nEstado atual da memória:")
    for i, particao in enumerate(particoes):
        status = particao["processo"] if particao["processo"] else "Livre"
        print(f"Partição {i+1} ({particao['tamanho']}): {status}")
    print()

# --- Teste da sequência ---
alocar("P1", 90)
alocar("P2", 140)
alocar("P3", 180)
liberar("P2")
alocar("P4", 100)
alocar("P5", 350)  # Vai falhar
mostrar()

# Mostra a fragmentação interna total
print(f"Fragmentação interna total: {sum(frag_total)}")