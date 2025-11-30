# Exercícios

## **1. Criar e escrever um arquivo de texto simples**

Crie um arquivo chamado `mensagem.txt` e escreva nele uma frase de sua escolha usando `with open()`.
Depois, abra novamente o arquivo e exiba o conteúdo na tela.

---

## **2. Ler um arquivo linha a linha (sem usar `.read()`)**

Dado um arquivo qualquer de texto longo (ex.: um pequeno texto literário), leia-o **linha por linha** usando um `for` e imprima as linhas numeradas:

```
1: primeira linha
2: segunda linha
...
```

Use `strip()` para limpar quebras de linha.

---

## **3. Copiar o conteúdo de um arquivo para outro**

Leia o conteúdo de um arquivo `origem.txt` e crie um arquivo `copia.txt` com o mesmo conteúdo.
Depois confirme que ambos têm exatamente o mesmo texto.

---

## **4. Criar um programa de "contador de palavras"**

Peça ao usuário um nome de arquivo.
O programa deve:

* abrir o arquivo
* contar quantas palavras existem
* exibir o total

Use tratamento de exceções para:

* arquivo não encontrado
* arquivo vazio
* permissões negadas

---

## **5. Criar e organizar diretórios com `os` ou `pathlib`**

Crie um script que:

1. Cria uma pasta chamada `projetos`
2. Dentro dela, cria três subpastas:

   * `entrada`
   * `processamento`
   * `saida`
3. Liste todas as pastas criadas

Faça usando **pathlib**.

---

## **6. Registrar logs simples em um arquivo**

Implemente um programa que:

* recebe entradas do usuário em um loop
* salva cada entrada em `logs.txt`
* finaliza quando o usuário digitar `"sair"`

Cada linha do log deve estar no formato:

```
[2025-11-27 13:45:10] Usuario digitou: exemplo
```

Use `datetime`.

---

## **7. Criar um programa que remove linhas duplicadas em um arquivo**

Receba um arquivo `.txt` contendo várias linhas repetidas.
Crie outro arquivo com **somente linhas únicas**, mantendo a ordem original.

Dicas:

* use um conjunto (`set`) para rastrear duplicatas
* cuidado para não alterar o arquivo original

---

## **8. Processar um arquivo CSV lendo valores como dicionários**

Dado um CSV com cabeçalho:

```
nome,idade,cidade
```

Leia o arquivo usando `csv.DictReader` e exiba na tela frases como:

```
Ana tem 30 anos e mora em São Paulo.
```

---

## **9. Criar um CSV a partir de uma lista de dicionários**

Dada uma lista:

```python
dados = [
    {"nome": "Ana", "idade": 30},
    {"nome": "João", "idade": 25},
    {"nome": "Marcos", "idade": 40},
]
```

Crie um arquivo `pessoas.csv` com cabeçalhos e uma linha para cada pessoa.

Use `DictWriter`.

---

## **10. Criar um programa de “Relatório de Gastos” usando CSV**

Crie um CSV chamado `gastos.csv` com as colunas:

```
descricao,valor
```

Depois escreva um script que:

1. lê o arquivo
2. soma todos os valores
3. monta um relatório como:

```
Relatório de Gastos
-------------------
Total de lançamentos: 7
Total gasto: R$ 1034.50
```

Esse exercício junta leitura de CSV, conversão de tipos e formatação.
