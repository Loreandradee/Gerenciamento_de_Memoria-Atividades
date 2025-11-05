# 📁 Q3 - ALGORITMO DE SUBSTITUIÇÃO DE PÁGINA FIFO

> 🌐 **NOTA:** Este arquivo e a pasta foram gerenciados e carregados via interface web do GitHub.

## 👤 Responsável

* **Aluno:** VANUSA DA SILVA DE ALMEIDA
* **Questão Prática:** Questão 3: Simulação do Algoritmo FIFO (First-In, First-Out)
* **Linguagem:** Java

---

## 📝 Descrição da Atividade (Parte B - Prática)

Este programa em Java simula o algoritmo de substituição de página **FIFO**. FIFO substitui a página que está na memória há mais tempo (a primeira a entrar).

Especificamente, o código implementa:

* Recebe como entrada o número de frames e a sequência de referências a páginas.
* Simula o carregamento e substituição de páginas, utilizando a regra FIFO (Queue/ArrayList).
* Exibe o estado dos frames, se houve Page Fault (falta) ou Page Hit (acerto) após cada referência.
* Conta e exibe o número total de faltas de página.
* Calcula e exibe a taxa final de faltas de página.

---

## ▶️ Instruções de Execução

**ATENÇÃO:** O código NÃO pode ser executado no GitHub Web. A execução deve ser feita no **Terminal Local** do seu computador.

1.  **Baixar e Descompactar:** O código-fonte está dentro de um arquivo ZIP (`Questão_03.zip`). É necessário descompactá-lo e navegar até o diretório da classe principal (provavelmente dentro de uma pasta `src/` ou similar).
2.  **Acessar:** Abra o Terminal (CMD, PowerShell ou Git Bash) e navegue até a pasta do código-fonte (onde está a classe principal, ex: `FifoPageReplacement.java`).

| Ação | Comando a ser Executado |
| :--- | :--- |
| **Compilação** | `javac [Nome da Classe Principal].java` (Ex: `javac FifoPageReplacement.java`) |
| **Execução** | `java [Nome da Classe Principal]` (Ex: `java FifoPageReplacement`) |

O código contém **comentários internos** detalhados, explicando o funcionamento da fila FIFO e o cálculo das estatísticas.
