# 📁 Q3 - ALGORITMO DE SUBSTITUIÇÃO DE PÁGINA FIFO

> 🌐 **NOTA:** Este arquivo e a pasta foram gerenciados e carregados via interface web do GitHub.

## 👤 Responsável

* **Aluno:** VANUSA DA SILVA DE ALMEIDA
* **Questão Prática:** Questão 3: Simulação do Algoritmo FIFO (First-In, First-Out)
* **Linguagem:** Java

---

## 📝 Descrição da Atividade (Parte B - Prática)

Este programa em Java simula o algoritmo de substituição de página **FIFO** (First-In, First-Out), que substitui a página que está na memória há mais tempo.

**O código implementa:**

* **Estruturas Eficientes:** Uso de `Queue` (para manter a ordem FIFO) e `Set` (para checagem rápida de presença).
* **Feedback em Tempo Real:** Exibe o estado atual dos frames, o status (Page Fault ou Hit) e a página substituída após cada referência.
* **Estatísticas Finais:** Calcula e exibe o número total e a taxa de faltas de página.
* **Tratamento de Erros:** Inclui tratamento para entradas não numéricas na sequência de referências.

---

## ▶️ Instruções de Execução

**ATENÇÃO:** O código NÃO pode ser executado no GitHub Web. A execução deve ser feita no **Terminal Local** do seu computador.

**Informações Cruciais:**
* **Arquivo Principal:** `FIFOPageReplacement.java`
* **Pacote:** `FifoJava` (O arquivo deve estar na pasta `FifoJava` dentro do seu diretório de código-fonte).
* **Formato de Entrada:** O programa espera a sequência de páginas separada por **vírgulas** (Ex: `7,0,1,2,0,3,0,4`).

1.  **Baixar e Descompactar:** O código-fonte está dentro de um arquivo ZIP. É necessário descompactá-lo e navegar até o diretório do projeto.
2.  **Acessar:** Abra o Terminal (CMD, PowerShell ou Git Bash) e navegue até a pasta **acima** da pasta `FifoJava`.

| Ação | Comando a ser Executado |
| :--- | :--- |
| **Compilação** | `javac FifoJava/FIFOPageReplacement.java` |
| **Execução** | `java FifoJava.FIFOPageReplacement` |

O código contém **comentários internos** detalhados, explicando o funcionamento da fila FIFO e o cálculo das estatísticas.
