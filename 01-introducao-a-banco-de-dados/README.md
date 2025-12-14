## Introdução ao módulo

Neste módulo, o objetivo não é só “aprender SQL” ou “instalar um banco”.
É entender **por que bancos de dados existem**, **como eles organizam informação** e **qual o papel deles dentro de uma aplicação moderna**.

Pensando já em APIs:

* o banco guarda o estado;
* a API orquestra acesso e regras;
* o cliente só enxerga o resultado.

Sem esse módulo bem sedimentado, qualquer aplicação cresce torta.

---

## Introdução a Banco de Dados

Um banco de dados é um **sistema organizado para armazenar, consultar, atualizar e proteger dados**.

Antes dos bancos, tudo era arquivo:

* CSVs espalhados,
* planilhas,
* texto puro.

Isso escala mal, quebra fácil e vira caos rapidamente.

Bancos de dados resolvem problemas como:

* concorrência (várias pessoas acessando ao mesmo tempo);
* integridade dos dados;
* performance em consultas grandes;
* segurança e controle de acesso;
* persistência confiável.

Em termos simples:
o banco é o **arquivo que sabe pensar**.

---

## Tipos de banco de dados

Existem várias famílias, cada uma com sua filosofia.

### Bancos Relacionais (SQL)

São baseados em:

* tabelas;
* linhas e colunas;
* relações entre dados;
* linguagem SQL.

Exemplos:

* PostgreSQL
* MySQL
* SQL Server
* Oracle
* SQLite

Características principais:

* esquema bem definido;
* integridade referencial (chaves primárias e estrangeiras);
* transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade).

São a escolha padrão para:

* sistemas corporativos;
* aplicações transacionais;
* APIs CRUD clássicas.

---

### Bancos Não Relacionais (NoSQL)

Aqui o foco muda: flexibilidade e escala horizontal.

Exemplos:

* MongoDB (documentos)
* Redis (chave-valor)
* Cassandra (colunar)
* Neo4j (grafos)

Eles sacrificam parte da rigidez dos relacionais em troca de:

* esquemas flexíveis;
* facilidade de escalar;
* performance em certos cenários específicos.

Falaremos mais deles daqui a pouco.

---

## Entendendo uma tabela

No modelo relacional, a **tabela** é a unidade central.

Você pode pensar nela como:

* uma planilha muito séria;
* onde cada linha é um registro;
* cada coluna é um atributo.

Exemplo mental: tabela `usuarios`

| id | nome    | email                                         | ativo |
| -- | ------- | --------------------------------------------- | ----- |
| 1  | Luciano | [luciano@email.com](mailto:luciano@email.com) | true  |
| 2  | Maria   | [maria@email.com](mailto:maria@email.com)     | false |

Conceitos fundamentais:

* **Linha (row)**: um registro individual.
* **Coluna (column)**: um campo com tipo definido.
* **Chave primária (PK)**: identifica unicamente cada linha.
* **Chave estrangeira (FK)**: referencia outra tabela.
* **Índices**: aceleram consultas.

Uma API bem projetada costuma mapear:

* um recurso REST ↔ uma tabela principal.

---

## Banco de dados não relacional

Bancos não relacionais não seguem o modelo rígido de tabelas relacionadas.

### Exemplo: MongoDB (documentos)

Em vez de tabelas, temos **coleções de documentos JSON**:

```json
{
  "_id": "abc123",
  "nome": "Luciano",
  "email": "luciano@email.com",
  "enderecos": [
    { "cidade": "São Paulo", "tipo": "residencial" }
  ]
}
```

Vantagens:

* esquema flexível;
* fácil armazenar dados aninhados;
* menos joins complexos.

Desvantagens:

* menos garantias de integridade;
* consultas complexas podem ser mais difíceis;
* nem sempre ideal para transações financeiras.

No mundo real:

* SQL resolve a maioria dos problemas.
* NoSQL resolve problemas específicos muito bem.

Escolher banco é engenharia, não moda.

---

## Tipos de dados

Tipos de dados definem **o que pode ser armazenado** em cada coluna.

Nos bancos relacionais, isso é crítico para:

* validação;
* performance;
* economia de espaço;
* integridade.

Tipos comuns:

* **Inteiros**: `INT`, `BIGINT`
* **Decimais**: `DECIMAL`, `NUMERIC`, `FLOAT`
* **Texto**: `VARCHAR`, `CHAR`, `TEXT`
* **Booleanos**: `BOOLEAN`, `BIT`
* **Datas e tempo**: `DATE`, `TIMESTAMP`, `DATETIME`
* **Binários**: `BLOB`, `BYTEA`
* **UUID**: identificadores únicos globais

Importante notar:

* tipo errado hoje = dor de cabeça amanhã;
* tipo bem escolhido ajuda o banco a otimizar consultas.

Quando você usar ORMs com FastAPI, esses tipos serão mapeados para tipos Python automaticamente.

---

## Entendendo o DBMS

DBMS significa **Database Management System**.

É o software que:

* gerencia o banco;
* controla acesso;
* executa consultas;
* garante integridade;
* otimiza performance.

Exemplos de DBMS:

* PostgreSQL → `postgres`
* SQL Server → `sqlservr`
* MySQL → `mysqld`
* SQLite → embutido na aplicação

Você **não acessa o banco diretamente**; sempre fala com o DBMS, que:

* interpreta SQL;
* decide planos de execução;
* cuida de locks, índices, transações.

Quando sua API se conecta ao banco, ela se conecta ao **DBMS**, não aos arquivos físicos do banco.

---

## Instalando o SQL Server

O SQL Server é um banco relacional da Microsoft, muito usado em ambientes corporativos.
Hoje ele roda tranquilamente em Linux e Docker, o que facilita bastante o desenvolvimento.

### Opção comum para desenvolvimento: Docker

Se você já usa Docker (como vimos em conversas anteriores), esse é o caminho mais limpo.

Exemplo conceitual:

```bash
docker run -e "ACCEPT_EULA=Y" \
           -e "SA_PASSWORD=SenhaForte123!" \
           -p 1433:1433 \
           --name sqlserver \
           -d mcr.microsoft.com/mssql/server:2022-latest
```

Isso sobe:

* SQL Server 2022
* porta padrão 1433
* usuário `sa`

Depois você pode conectar usando:

* Azure Data Studio
* DBeaver
* SQL Server Management Studio (em Windows)
* ou drivers Python (`pyodbc`, `pymssql`).

### Instalação nativa (Linux)

Também é possível instalar direto no sistema:

* adicionar repositório da Microsoft;
* instalar o pacote `mssql-server`;
* rodar o assistente de configuração.

Para **ambiente de estudo**, Docker costuma ser mais rápido, isolado e reversível.

---

## Conexão com o que vem depois

Esse módulo prepara o terreno para:

* entender como uma API persiste dados;
* escolher entre SQL e NoSQL com consciência;
* usar ORMs sem “fé cega”;
* modelar tabelas alinhadas aos recursos REST.

No próximo passo natural, a conversa evolui para:

* modelagem relacional;
* SQL básico (SELECT, INSERT, UPDATE, DELETE);
* e depois a integração disso tudo com FastAPI usando um ORM.

Aqui, você não está só aprendendo banco de dados.
Está aprendendo a **pensar dados como parte viva da arquitetura**.
