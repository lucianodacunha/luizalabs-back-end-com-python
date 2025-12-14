Perfeito. Hora de transformar teoria em **músculo cognitivo** 💪
Esses exercícios foram pensados como uma progressão: começam mecânicos, mas terminam exigindo **pensamento arquitetural**, não só sintaxe.

A ideia não é correr — é entender **o porquê de cada decisão**.

---

### 1. Conexão segura e ciclo de vida

Crie um script Python que:

* abra uma conexão com um banco SQLite;
* execute uma consulta simples (`SELECT 1`);
* feche a conexão corretamente, mesmo que ocorra uma exceção.

Objetivo oculto: treinar uso correto de `try / finally` ou `with`.

---

### 2. Criação de tabela com integridade

Crie uma tabela `clientes` com:

* `id` (chave primária);
* `nome` (não nulo);
* `email` (único);
* `ativo` (booleano).

Depois:

* execute o script duas vezes;
* garanta que ele não quebre nem recrie a tabela.

Objetivo: entender `IF NOT EXISTS` e integridade básica.

---

### 3. Inserção com parâmetros

Implemente uma função `criar_cliente(nome, email, ativo)` que:

* insira um registro usando parâmetros;
* nunca use concatenação de string;
* faça `commit` corretamente.

Depois, tente inserir dois clientes com o mesmo email e observe o erro.

Objetivo: segurança + violação de constraint.

---

### 4. Tratamento de exceções do banco

A partir do exercício anterior:

* capture a exceção de integridade (email duplicado);
* retorne uma mensagem de erro amigável;
* garanta que a transação seja revertida.

Objetivo: entender rollback e exceções específicas do DB-API.

---

### 5. Consulta e leitura de resultados

Crie uma função `listar_clientes()` que:

* execute um `SELECT * FROM clientes`;
* imprima os resultados linha por linha;
* depois altere o código para usar `fetchone()` e `fetchmany()`.

Objetivo: entender as formas de consumo do cursor.

---

### 6. Uso de `row_factory` (ou cursor equivalente)

Altere a conexão para que:

* cada linha seja retornada como um “dicionário”;
* você possa acessar campos por nome (`row["email"]`);
* gere uma lista de dicionários pronta para JSON.

Objetivo: preparar o terreno para integração com API.

---

### 7. Atualização e remoção seguras

Implemente duas funções:

* `desativar_cliente(email)`
* `remover_cliente(id)`

Regras:

* sempre use `WHERE`;
* valide se algum registro foi afetado;
* faça `commit` apenas quando fizer sentido.

Objetivo: evitar `UPDATE` / `DELETE` destrutivos.

---

### 8. Inserção em lote com transação

Receba uma lista de clientes e:

* insira todos usando `executemany()`;
* se qualquer inserção falhar, nenhum cliente deve ser salvo;
* use transação explícita (`commit` / `rollback`).

Objetivo: atomicidade e performance.

---

### 9. Simulação de falha e consistência

Crie duas tabelas:

* `clientes`
* `pedidos` (com `cliente_id` como FK)

Implemente uma função que:

* cria um cliente;
* cria um pedido para esse cliente;
* simule um erro proposital na segunda inserção.

Verifique:

* se o cliente ficou salvo ou não;
* ajuste o código para garantir consistência.

Objetivo: entender transações como regra de negócio.

---

### 10. Logging e isolamento de erros

Implemente um pequeno módulo que:

* execute uma operação de banco;
* capture erros;
* registre o erro com `logging`;
* retorne apenas uma mensagem genérica ao “usuário final”.

Desafio extra:

* logar SQL e parâmetros **sem expor isso na resposta**.

Objetivo: separar diagnóstico interno de comunicação externa.

---

### Como usar esses exercícios

Sugestão de abordagem:

* use **SQLite** para não perder tempo com setup;
* resolva cada exercício em um arquivo separado;
* depois refatore tudo em um pequeno “mini repositório de dados”;
* só então pense em ORM.
