# 📁 Q4 - GARBAGE COLLECTION EM PYTHON

> 🌐 **NOTA:** Este arquivo e a pasta foram carregados via interface web do GitHub.

## 👤 Responsável

* **Aluno:** LORENA ANDRADE DE SOUZA
* **Questão Prática:** Questão 4: Demonstração do Funcionamento do Garbage Collector
* **Linguagem:** Python

---

## 📝 Descrição da Atividade (Parte B - Prática)

Este programa em Python demonstra o funcionamento dos dois mecanismos principais de Coleta de Lixo (Garbage Collection - GC) da linguagem: **Contagem de Referências** e **Coleta Geracional**.

Especificamente, o código implementa:

* Criação de uma classe `Objeto` com métodos `__init__` e `__del__` para rastrear criação/destruição.
* **Cenário 1:** Demonstração da destruição automática imediata por Contagem de Referências (`del`).
* **Cenário 2:** Demonstração da falha na Contagem de Referências com **Referências Circulares**, e a necessidade de `gc.collect()`.
* Uso de `sys.getrefcount()` para mostrar a contagem de referências.
* Exibição das estatísticas do coletor de lixo com `gc.get_stats()`.
* Análise final da diferença entre a coleta por Contagem de Referências e a Coleta Geracional.

---

## ▶️ Instruções de Execução

**ATENÇÃO:** O código NÃO pode ser executado no GitHub Web. A execução deve ser feita no **Terminal Local** do seu computador.

1.  **Baixar:** Faça o download do repositório para sua máquina.
2.  **Acessar:** Abra o Terminal (CMD, PowerShell ou Git Bash) e navegue até a pasta **`Questão04_gc_Python/`**.
3.  **Arquivo Principal:** `Questão_04.py`

| Ação | Comando a ser Executado |
| :--- | :--- |
| **Compilação** | N/A (Linguagem Interpretada) |
| **Execução** | `python Questão_04.py` |

O código contém **comentários internos** detalhados, explicando a lógica de alocação de memória simulada e o significado de cada etapa da coleta.
