# Gerenciamento de Despesas Simples com Python

Este projeto é uma ferramenta Python simples para **gerenciar e relatar despesas mensais**. Ele inclui um script principal para calcular o total das despesas e um script de teste automatizado para validar se esses valores estão dentro de limites aceitáveis.

Além disso, o projeto utiliza **GitHub Actions** para configurar um fluxo de trabalho de Integração Contínua (CI) que executa os testes automaticamente a cada `push` ou `pull request` na branch principal, garantindo a integridade do cálculo das despesas.

---

## 🌟 Estrutura do Projeto

* `codigo.py`: Contém a lógica principal para armazenar as despesas e calcular o total.
* `teste.py`: Script de teste que verifica se o total das despesas está dentro de uma faixa predefinida.
* `.github/workflows/testar_codigo_python.yml`: Configuração do workflow do GitHub Actions para automatizar a execução dos testes.

---

## 🚀 Como Usar

### Executando o Relatório de Despesas

Para rodar o script principal e ver o relatório de despesas, basta executar o arquivo `codigo.py`:

1.  Certifique-se de ter **Python** instalado em sua máquina.
2.  Navegue até o diretório do projeto no seu terminal.
3.  Execute o script:

    ```bash
    python codigo.py
    ```

    Isso imprimirá um relatório simples com o total das despesas mensais definidas no `codigo.py`.

### Executando os Testes Manualmente

Para verificar a integridade do cálculo das despesas localmente, você pode rodar o script de teste:

1.  Navegue até o diretório do projeto no seu terminal.
2.  Execute o script de teste:

    ```bash
    python teste.py
    ```

    O script informará se o teste passou (total dentro da faixa esperada) ou falhou (total fora da faixa).

---

## 🧪 Testes Automatizados com GitHub Actions

Este projeto está configurado para utilizar o **GitHub Actions** para automação de testes. Sempre que houver um `push` (envio de código) ou um `pull request` para a branch `main` do repositório, o workflow definido em `.github/workflows/testar_codigo_python.yml` será acionado automaticamente.

### Como funciona:

1.  **Gatilho:** `push` ou `pull_request` na branch `main`.
2.  **Ambiente:** O teste é executado em um ambiente `ubuntu-latest`.
3.  **Etapas:**
    * **Baixar o código:** O repositório é clonado para o ambiente de execução.
    * **Configurar Python:** O ambiente é configurado com Python 3.10.
    * **Executar Teste:** O comando `python teste.py` é executado, e o resultado (passou/falhou) é reportado no GitHub Actions.

Você pode acompanhar o status das execuções dos testes na aba **"Actions"** do seu repositório no GitHub.

## 📄 Licença

Este projeto é de código aberto e está disponível . Para mais detalhes, consulte o arquivo `LICENSE` no repositório.

---
