# 📁 Q1 - ALOCAÇÃO ESTÁTICA VS. DINÂMICA

> 🌐 **NOTA:** Este arquivo e a pasta foram gerenciados e carregados via interface web do GitHub.

## 👤 Responsável

* **Aluno:** GABRIEL GUEDES ARCHANJO
* **Questão Prática:** Questão 1: Implementação em C de Alocação Estática vs. Dinâmica
* **Linguagem:** C

---

## 📝 Descrição da Atividade (Parte B - Prática)

Este programa em C demonstra a diferença fundamental entre a alocação de memória na pilha (Stack) e a alocação de memória no heap (Heap).

Especificamente, o código implementa:

* Declaração e preenchimento de um array estático (na Stack) de 5 inteiros.
* Alocação e preenchimento de um array dinâmico (no Heap) de 10 inteiros usando `malloc`.
* Cálculo e exibição dos endereços de memória de ambos os arrays, provando que estão em áreas distintas.
* Verificação obrigatória se a alocação dinâmica foi bem-sucedida.
* Liberação correta da memória alocada dinamicamente com `free`.

---

## ▶️ Instruções de Execução

**ATENÇÃO:** O código NÃO pode ser executado no GitHub Web. A execução deve ser feita no **Terminal Local** do seu computador.

1.  **Baixar:** Faça o download do repositório para sua máquina.
2.  **Acessar:** Abra o Terminal (CMD, PowerShell ou Git Bash) e navegue até a pasta **`Questão01_alocacao_C/`**.
3.  **Arquivo Principal:** `Questão_01.c`

| Ação | Comando a ser Executado |
| :--- | :--- |
| **Compilação** | `gcc Questão_01.c -o q1_exec` |
| **Execução** | `./q1_exec` |

O código contém **comentários internos** detalhados, explicando a lógica de alocação e a interpretação dos endereços de memória.
