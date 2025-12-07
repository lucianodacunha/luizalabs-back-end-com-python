# Fundamentos de POO em Soluções Digitais

## 1. RoboMensagem POO 2.0

A startup InovaTec lançou seu primeiro protótipo de robô assistente pessoal, chamado RoboMensagem. Este robô é capaz de ajudar engenheiros a organizar suas comunicações diárias de forma eficiente. Para testar suas habilidades de Programação Orientada a Objetos, a equipe de desenvolvimento decidiu implementar um sistema onde cada mensagem enviada ao robô é processada por um objeto da classe Mensagem. Cada Mensagem possui um remetente e um conteúdo, e o RoboMensagem deve ser capaz de identificar quem enviou a mensagem e qual é o conteúdo transmitido, imprimindo ambas as informações no formato correto.

Sua tarefa é implementar a classe Mensagem com dois atributos (remetente e conteudo) e um método chamado exibir, que retorna as informações formatadas como ": ".

Todas as operações devem ser encapsuladas na classe e não é permitido utilizar bibliotecas externas além da biblioteca padrão de sua linguagem.

### Entrada

A primeira linha contém o nome do remetente. A segunda linha contém o conteúdo da mensagem, ambos sem acentos ou caracteres especiais.

O comprimento de cada linha está limitado ao máximo de 69 caracteres ASCII.

### Saída

Imprima uma única linha no formato ": ", respeitando exatamente este padrão.

A saída não deve conter espaços extras, aspas ou acentos e deve exibir apenas a mensagem processada pelo objeto criado.

### Exemplos

A tabela abaixo apresenta exemplos de entrada e saída:

|Entrada| 	Saída|
|---|---|
|Maria<br>Bom dia equipe|Maria: Bom dia equipe|
|Joao<br>Reuniao adiada para amanha |Joao: Reuniao adiada para amanha|
|Luiz23<br>Teste do sistema completo |Luiz23: Teste do sistema completo|

## 2. RoboNomeador 3000

Na cidade futurista de Inovapolis, engenheiros trabalham em uma startup dedicada à criação de robôs inteligentes para ajudar pequenas tarefas diárias. Como parte da competição anual de tecnologia, sua equipe precisa construir um sistema que dê nomes exclusivos para cada novo protótipo fabricado, unindo duas palavras de identificação. Para garantir flexibilidade e organização, a equipe decidiu usar conceitos de Programação Orientada a Objetos para representar cada robô. Sua missão é implementar o núcleo desse sistema: uma classe responsável por armazenar os dois identificadores de cada robô e gerar corretamente o nome composto.

Sua solução deve criar uma classe que receba dois nomes (modelos) na inicialização e disponibilize um método para exibir o nome completo do robô no formato correto. O objetivo é demonstrar domínio básico de POO criando e utilizando objetos, métodos e construtores. As palavras informadas não terão espaços nem acentuação e devem ser unidas por um hífen.

### Entrada

Uma linha contendo duas strings separadas por espaço, representando os modelos do robô (apenas caracteres ASCII sem acentuação, mínimo 1 e máximo 30 cada).

### Saída

Uma única linha contendo o nome completo do robô, no formato modelo1-modelo2 (sem espaços adicionais e sem acentuação), tudo em uma string.

### Exemplos

A tabela abaixo apresenta exemplos de entrada e saída:
|Entrada| 	Saída|
|---|---|
|nano chip| 	nano-chip|
|eco bot |	eco-bot|
|laser rover| 	laser-rover|