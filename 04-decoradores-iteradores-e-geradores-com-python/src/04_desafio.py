"""
=======
Desafio 
=======

Implementar as seguintes funcionalidades do sistema:

Decorador de log
----------------

Implemente um decorador que seja aplicado a todas as funções de transações
(depósito, saque, criação de conta, etc).
Esse decorador deve registrar (printar) a data e hora de cada transação, bem 
como o tipo de transação.

Gerador de relatórios
---------------------

Crie um gerador que permita iterar sobre as transações de uma conta e retorne,
uma a uma, as transações que foram realizadas. Esse gerador, deve também ter uma
forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques
ou apenas depósitos).

Iterador personalizado
----------------------

Implemente um iterador personalizado ContaIterador que permita iterar sobre 
todas as contas do banco, retornando as informações básicas (número, saldo
atual, etc).

TODO: 
-----

- Revisar o módulo
- Resolver o desafio após concluir o módulo de Orientação a Objetos.
- Refazer o teste do módulo.

Link para o módulo:
-------------------

https://web.dio.me/track/luizalabs-back-end-com-python/course/decoradores-iteradores-e-geradores-com-python/learning/52c6e3c8-23f9-48e6-94c5-1feedaab3160?autoplay=1

"""