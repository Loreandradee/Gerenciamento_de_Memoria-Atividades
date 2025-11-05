import time
import gc

j=5 #variavel para definir quantia de repetições

#==============================< pilha >===================================

def pilha(n): #função chamada pilha para organizar melhor o código
    i=0
    for _ in range(n): #No for que se repetirá 1000000 ele retorna i + 1 a cada repetição
        i+=1 #incrementa o valor de i a ele mesmo
    return i #retorna o i

#==============================< heap >====================================

def heap(n):#função chamada heap para organizar melhor o código
    lista = [] #criamos uma lista para armazenar os inteiros do for abaixo
    for i in range(n): #No for que se repetirá 1000000 ele adicionará o número em i na lista
     i+= 1
    lista.append(i)
        
    del lista  #Ao finalizar o for, a lista será deletada e recuperada por gc.collect
    gc.collect()  
    
def executarTeste(p):
    #listas pra armazenar os valor obtidos e em seguida fazer as médias
    listatempoHeap = [] 
    listatempoPilha = []
    for _ in range(p):
        n = 1000000 #variavel no valor de um milhão

        # Tempo da pilha
        inicio = time.time()
        pilha(n)
        fim = time.time()
        tempoPilha = fim - inicio
        listatempoPilha.append(tempoPilha)
        
        # Tempo do heap
        inicio = time.time()
        heap(n)
        fim = time.time()
        tempoHeap = fim - inicio
        listatempoHeap.append(tempoHeap)
        
         # Cálculo das médias
    mediaPilha = sum(listatempoPilha) / p
    mediaHeap = sum(listatempoHeap) / p

    print(f"\nMedia de tempo da pilha (stack): {mediaPilha:.5f} segundos")
    print(f"Media de tempo do heap: {mediaHeap:.5f} segundos")

    # Comparação e percentual
    if mediaHeap > mediaPilha:
        percentual = ((mediaHeap - mediaPilha) / mediaPilha) * 100
        print(f"A pilha foi mais rapida com {percentual:.2f}% de vantagem sobre o heap.")
    else:
        percentual = ((mediaPilha - mediaHeap) / mediaHeap) * 100
        print(f"O heap foi mais rapido com {percentual:.2f}% de vantagem sobre a pilha.")

    # Explicação teórica
    print("\nExplicacao teorica:")
    print("A alocacao na pilha eh geralmente mais rapida porque envolve apenas mover o ponteiro de pilha,")
    print("enquanto a alocacao no heap requer gerenciamento mais complexo, como busca por espaco livre e coleta de lixo.")
    print("Alem disso, variaveis locais na pilha sao automaticamente desalocadas ao sair da funcao,")
    print("enquanto objetos no heap exigem gerenciamento manual ou coleta de lixo.")


            
executarTeste(j)