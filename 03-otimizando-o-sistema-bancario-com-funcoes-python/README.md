# Sistema Bancário Simples em Python

Este projeto é uma simulação de um sistema bancário básico em modo texto, desenvolvido em Python.  
O objetivo é praticar conceitos fundamentais de lógica de programação, controle de fluxo, variáveis e interação com o usuário.

## 🎯 Funcionalidades Atuais

O sistema oferece as seguintes operações:

- **[d] Depositar**  
  Permite ao usuário realizar depósitos em conta, atualizando o saldo e registrando o histórico no extrato.

- **[s] Sacar**  
  Permite saques, respeitando:
  - saldo disponível
  - limite máximo por saque
  - limite máximo diário de saques

- **[e] Extrato**  
  Exibe o histórico de movimentações (depósitos e saques) e o saldo atual.

- **[q] Sair**  
  Encerra o programa.

---

## 🧩 Regras de Negócio Implementadas

### Depósito

- O usuário informa um valor.
- O valor deve ser **maior que zero**.
- Em caso de valor válido:
  - o saldo é atualizado: `saldo += valor`
  - o extrato recebe uma nova linha com a operação:
    - `Depósito: R$ <valor>`
- Em caso de valor inválido:
  - é exibida a mensagem:  
    `Operação falhou! O valor informado é inválido.`

---

### Saque

O saque está sujeito a três validações:

1. **Saldo suficiente**  
   - Não é permitido sacar mais do que o saldo disponível.
   - Condição: `valor > saldo`
   - Mensagem em caso de falha:  
     `Operação falhou! Você não tem saldo suficiente.`

2. **Limite por operação**  
   - Cada saque possui um limite máximo definido pela variável `limite`.
   - Condição: `valor > limite`
   - Mensagem em caso de falha:  
     `Operação falhou! O valor do saque excede o limite.`

3. **Quantidade máxima de saques diários**  
   - Existe um limite diário de saques, definido em `LIMITE_SAQUES`.
   - A variável `numero_saques` controla quantos já foram feitos.
   - Condição: `numero_saques >= LIMITE_SAQUES`
   - Mensagem em caso de falha:  
     `Operação falhou! Número máximo de saques excedido.`

4. **Validação do valor**  
   - O valor do saque deve ser **maior que zero**.
   - Em caso de sucesso:
     - o saldo é atualizado: `saldo -= valor`
     - o extrato recebe nova linha: `Saque: R$ <valor>`
     - `numero_saques` é incrementado: `numero_saques += 1`
   - Em caso de valor inválido:
     - é exibida a mensagem:  
       `Operação falhou! O valor informado é inválido.`

---

### Extrato

- Ao selecionar a opção `[e]`:
  - É exibido um cabeçalho de extrato.
  - Se **não houver movimentações**, o sistema mostra:  
    `Não foram realizadas movimentações.`
  - Caso contrário, imprime todo o conteúdo da variável `extrato`.
  - Em seguida, exibe o saldo atual:
    - `Saldo: R$ <saldo>`

---

## 🧮 Variáveis Principais

- `saldo`: controla o saldo atual da conta (inicia em `0`).
- `limite`: valor máximo permitido por saque (inicia em `500`).
- `extrato`: string que acumula o histórico de operações.
- `numero_saques`: contador de saques realizados na sessão.
- `LIMITE_SAQUES`: constante que define o número máximo de saques permitidos (inicia em `3`).

---

## 🔁 Fluxo Geral do Programa

O programa funciona em um loop infinito (`while True`), exibindo o menu e esperando a escolha do usuário:

1. Exibe o menu com as opções: `[d] [s] [e] [q]`.
2. Lê a opção com `input(menu)`.
3. De acordo com a opção:
   - `"d"` → executa fluxo de depósito
   - `"s"` → executa fluxo de saque
   - `"e"` → exibe extrato
   - `"q"` → encerra o loop com `break`
   - qualquer outra entrada → exibe mensagem de operação inválida

O loop só é interrompido quando o usuário escolhe a opção `[q] Sair`.

---

## ▶️ Como Executar o Programa

1. Certifique-se de ter o Python instalado (3.x).
2. Salve o código em um arquivo, por exemplo: `sistema_bancario.py`.
3. No terminal, execute:

```bash
python sistema_bancario.py
