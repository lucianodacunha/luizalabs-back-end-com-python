# Desafio de Código

## 1. RoboFormatador 2.0

Na futurística cidade de Tecnos, a equipe do Laboratório de Inovação está desenvolvendo um robô que processa comandos de texto enviados por usuários. Para garantir clareza nos logs e troca de dados, o robô deve ser capaz de padronizar e aprimorar mensagens usando funções bem definidas, seguindo boas práticas de programação. Seu desafio é ajudar a equipe do laboratório a criar uma função que recebe uma mensagem enviada ao robô e retorna a mesma mensagem:

1. sem espaços extras no início ou fim, 
2. com todas as letras minúsculas, e 
3. com apenas um único espaço separando as palavras.

Implemente esta função seguindo boas práticas (clareza, reutilização e modularização) e sem utilizar bibliotecas externas. Certifique-se de que a função trate corretamente mensagens já padronizadas ou compostas apenas de espaços.

## Entrada

Uma única linha contendo uma mensagem (string) enviada ao robô. A mensagem pode conter letras maiúsculas ou minúsculas, espaços múltiplos entre palavras ou ao redor, e pode estar vazia ou conter apenas espaços.

## Saída

Uma única linha contendo a mensagem processada: sem espaços extras no início/fim, todas as letras em minúsculo, e com apenas um espaço separando cada palavra. Se a entrada for vazia ou composta apenas por espaços, a saída deve ser uma linha vazia.

## Exemplos

A tabela abaixo apresenta exemplos de entrada e saída:

|Entrada|Saída|
|---|--|
|   Bem  Vindo Ao  LAB         |bem vindo ao lab|
| INOVAR     sempre            |inovar sempre|
|    Essa   Eh Uma  LINHA     Teste    |essa eh uma linha teste|


## 2. Identificador de Gadget

No laboratório de inovação TechDreams, engenheiros trabalham dia e noite criando gadgets incríveis para facilitar o dia a dia das pessoas. No entanto, as equipes têm enfrentado um pequeno problema: identificar rapidamente a categoria de cada gadget recém-desenvolvido a partir de seu código. Para otimizar esse processo e incentivar boas práticas de programação, a líder de projetos, Zoe, propôs um desafio aos novos desenvolvedores. Eles devem criar uma função clara e bem definida que, ao receber como entrada um código de gadget, devolve a categoria correta. Isso garantirá um código fácil de entender, manter e reutilizar no futuro.

Sua missão é implementar uma função que receba uma string representando o código de um gadget e retorne a categoria correspondente. Considere estas categorias: códigos que comecem com “T” são “tablet”, com “P” são “phone” e com “N” são “notebook”. Caso não pertença a nenhuma dessas categorias, retorne “unknown”. O objetivo é mostrar como funções facilitam o código limpo e reutilizável, elementos essenciais em ambientes de inovação constante.

Respeite os formatos de entrada e saída indicados abaixo e não use bibliotecas externas.

## Entrada

Uma única string com o código do gadget (sem espaços). O código pode conter letras e/ou números.

## Saída

Uma única palavra indicando a categoria do gadget: “tablet”, “phone”, “notebook” ou “unknown”.

## Exemplos

A tabela abaixo apresenta exemplos de entrada e saída:
|Entrada|Saída|
|---|---|
|T12345X|tablet|
|P45YTS|phone|
|R2123Z|unknown|