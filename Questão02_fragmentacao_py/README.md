# 📁 Q2 - SIMULAÇÃO DE FRAGMENTAÇÃO DE MEMÓRIA

> 🌐 **NOTA:** Este arquivo e a pasta foram carregados via interface web do GitHub.

## 👤 Responsável

* **Aluno:** DANIEL FERNANDO ABREU DE MORAES
* **Questão Prática:** Questão 2: Simulação de Gerenciador com Partições Fixas (First-Fit)
* **Linguagem:** Python

---

## 📝 Descrição da Atividade (Parte B - Prática)

Este programa em Python simula um gerenciador de memória usando o esquema de **partições fixas** com o algoritmo de alocação **First-Fit**.

Especificamente, o código implementa:

* Criação de 5 partições fixas de tamanhos definidos (100, 150, 200, 250, 300).
* Funções `alocar_processo()` e `liberar_processo()` baseadas na estratégia First-Fit.
* Cálculo e exibição da **Fragmentação Interna** (espaço desperdiçado) após cada alocação.
* Tratamento para quando não há partição disponível.
* Teste de uma sequência específica de alocações e liberações (P1, P2, P3, Liberar P2, P4, Tentar P5).

---

## ▶️ Instruções de Execução

**ATENÇÃO:** O código NÃO pode ser executado no GitHub Web. A execução deve ser feita no **Terminal Local** do seu computador.

1.  **Baixar:** Faça o download do repositório para sua máquina.
2.  **Acessar:** Abra o Terminal (CMD, PowerShell ou Git Bash) e navegue até a pasta **`Questão02_fragmentacao_py/`**.
3.  **Arquivo Principal:** `Questão_02.py`

| Ação | Comando a ser Executado |
| :--- | :--- |
| **Compilação** | N/A (Linguagem Interpretada) |
| **Execução** | `python Questão_02.py` |

O código contém **comentários internos** detalhados, explicando o cálculo da fragmentação e a lógica do First-Fit.
