# Boas Práticas para APIs RESTful

## Introdução

APIs RESTful são o “esqueleto” da maioria das aplicações modernas: web, mobile, integrações entre sistemas, microserviços, etc.
A ideia das boas práticas é bem pragmática: não é frescura, é sobrevivência. Quando a API começa a crescer, se ela não foi pensada com cuidado, vira um *frankenstein* difícil de manter.

Boas práticas servem para:

* facilitar leitura e compreensão das rotas;
* tornar a API previsível (você “chuta” o endpoint e acerta);
* evitar conflitos e gambiarras na evolução da aplicação;
* facilitar documentação, testes e uso por terceiros.

---

## Contextualizando: o que são APIs RESTful

REST é um **estilo arquitetural** para construção de APIs.
Uma API RESTful, em resumo:

* trabalha com **recursos** (usuários, pedidos, produtos);
* usa **HTTP** de forma semântica (GET, POST, PUT, PATCH, DELETE);
* é normalmente **stateless**: cada requisição carrega tudo o que precisa;
* retorna representações de recursos (normalmente JSON).

Exemplo de recurso:

* `/usuarios` → coleção
* `/usuarios/123` → recurso específico

FastAPI é perfeito para isso: você pensa em “recursos e operações” e mapeia isso para rotas + métodos.

---

## Por que seguir boas práticas

Três motivos bem diretos:

1. **Previsibilidade**
   Quando alguém vê `/v1/usuarios/123/pedidos`, já sabe o que esperar sem ler documentação.

2. **Manutenibilidade**
   Com rotas, verbos e respostas padronizadas, é mais fácil:

   * refatorar código;
   * dividir trabalho entre equipes;
   * evoluir versões.

3. **Integração**
   Quem consome sua API (outra equipe, app mobile, parceiro externo) não precisa entrar em contato com você a cada requisição diferente. A própria estrutura da API “fala”.

---

## Utilização de substantivos em rotas

Regra de ouro: **rotas representam recursos → use substantivos, preferencialmente no plural**.

✅ Bom:

* `GET /usuarios`
* `GET /usuarios/10`
* `POST /usuarios`
* `GET /pedidos/2025/itens`

❌ Ruim:

* `GET /getUsuarios`
* `POST /criarUsuario`
* `DELETE /deletarUsuario`

O verbo da ação vem do **método HTTP**, não da URL. A URL diz *“O quê?”*, o verbo diz *“Fazer o quê com isso?”*.

Outros detalhes comuns:

* usar **kebab-case** ou **snake_case**?
  Em rotas, costuma-se usar **kebab-case**:
  `/relatorios-financeiros` é mais comum que `/relatorios_financeiros`.

---

## Utilização de métodos HTTP

Os métodos HTTP devem ser usados como semântica de ação sobre o recurso:

* **GET** – obter recurso(s)
  `GET /usuarios` → lista usuários
  `GET /usuarios/10` → detalhes do usuário 10

* **POST** – criar novo recurso
  `POST /usuarios` → cria um novo usuário

* **PUT** – substituir o recurso inteiro
  `PUT /usuarios/10` → atualiza usuário 10 com os dados enviados, substituindo tudo

* **PATCH** – atualizar parcialmente o recurso
  `PATCH /usuarios/10` → atualiza só os campos enviados

* **DELETE** – remover recurso
  `DELETE /usuarios/10` → exclui usuário 10

Conceito importante:

* **Idempotência**:

  * GET, PUT, DELETE devem ser idempotentes (mesma requisição várias vezes → mesmo resultado).
  * POST geralmente **não** é idempotente (postar duas vezes → dois recursos criados).

---

## Hierarquia e aninhamento em rotas

Use hierarquia para representar relações entre recursos.

Exemplo: Usuário → Pedidos

* `GET /usuarios/10/pedidos` → pedidos do usuário 10
* `POST /usuarios/10/pedidos` → cria pedido para o usuário 10
* `GET /usuarios/10/pedidos/55` → pedido 55 do usuário 10

Cuidados:

* evite **aninhamento profundo**:

  * ruim: `/empresas/1/filiais/2/departamentos/3/usuarios/4/projetos/5/tarefas/6`
  * melhor: parar em 2 ou 3 níveis e usar query params quando ficar complexo:

    * `/departamentos/3/usuarios`
    * `/tarefas?projeto_id=5&usuario_id=4`

Regra prática: se você passou de 3 níveis, já está com cheirinho de overdesign.

---

## Nome das ações

Algumas ações não se encaixam em CRUD puro (ativar conta, resetar senha, etc.). Aí sim pode aparecer verbo na rota, **mas como sub-recurso de ação**:

* `POST /usuarios/10/ativar`
* `POST /usuarios/10/resetar-senha`
* `POST /pedidos/55/cancelar`

Ainda assim, o mundo REST mais purista às vezes modela isso como alteração de estado:

* `PATCH /usuarios/10` com body `{ "ativo": true }`
* `PATCH /pedidos/55` com body `{ "status": "cancelado" }`

Ambas as abordagens são usadas na prática; o importante é ser **consistente**.

---

## Versionamento de rotas

Você não quer quebrar todo mundo quando mudar a API.
Por isso, versionar é essencial.

Forma mais comum (e simples):

* `/v1/usuarios`
* `/v1/pedidos`
* `/v2/usuarios`

Quando sai a versão 2:

* cliente antigo continua usando `/v1/...`;
* cliente novo consome `/v2/...`.

Outras abordagens (mais avançadas, mas comuns em APIs grandes):

* versão em header: `Accept: application/vnd.minhaapi.v1+json`
* versionamento por feature flag ou por campos.

Para cenário de bootcamp, o padrão **`/v1`, `/v2` no caminho** resolve 99% dos casos.

---

## Parâmetros de consulta (query params)

**Path params** → identificam recurso.
**Query params** → refinam, filtram, ordenam, paginam.

Exemplos:

Listar usuários com filtros:

* `GET /v1/usuarios?ativo=true`
* `GET /v1/usuarios?perfil=admin`

Paginação:

* `GET /v1/usuarios?page=2&limit=20`

Ordenação:

* `GET /v1/produtos?sort=preco` (ascendente)
* `GET /v1/produtos?sort=-preco` (descendente)

Busca:

* `GET /v1/produtos?search=mouse`

Boas práticas:

* Seja consistente nos nomes: `page`, `limit`, `sort`, `order`, `filter`, etc.
* Evite query param controlando comportamento bizarro da API, tipo `?delete_all=true` numa rota GET (isso é um crime contra a ergonomia).

---

## Tratamento de erros

Erro bem tratado é sinal de API profissional.

Pontos importantes:

1. **Use códigos HTTP corretos**

   * 200/201/204 → sucesso
   * 400 → requisição inválida (erro do cliente: payload malformado, etc.)
   * 401 → não autenticado
   * 403 → sem permissão
   * 404 → não encontrado
   * 409 → conflito (ex.: tentar criar algo que já existe)
   * 422 → erro de validação de dados (muito usado em APIs modernas, e o FastAPI adora esse)
   * 500+ → erro do servidor

2. **Estruture o corpo do erro**
   Um padrão comum:

   ```json
   {
     "error": {
       "code": "USER_NOT_FOUND",
       "message": "Usuário não encontrado.",
       "details": {
         "user_id": 123
       }
     }
   }
   ```

   Ou mais direto:

   ```json
   {
     "code": "VALIDATION_ERROR",
     "message": "Campos inválidos.",
     "errors": [
       { "field": "email", "message": "Formato inválido." },
       { "field": "senha", "message": "Mínimo 8 caracteres." }
     ]
   }
   ```

3. **Não exponha stack trace e detalhes internos em produção**

   * Nada de vazar nome de tabela, stack do Python, etc.
   * Logue internamente, responda de forma limpa externamente.

FastAPI já tem um ótimo tratamento base de erros de validação; o ideal é padronizar o formato de erro customizado conforme sua API.

---

## Exemplo completo de estrutura de rotas RESTful

Vamos imaginar uma mini API de e-commerce: **Usuários**, **Produtos**, **Pedidos**.
Versão: `v1`.

### Usuários

* `GET    /v1/usuarios` → lista usuários (com paginação)
* `POST   /v1/usuarios` → cria usuário
* `GET    /v1/usuarios/{usuario_id}` → detalha usuário
* `PUT    /v1/usuarios/{usuario_id}` → atualiza usuário (substituição completa)
* `PATCH  /v1/usuarios/{usuario_id}` → atualização parcial
* `DELETE /v1/usuarios/{usuario_id}` → remove usuário

Ações específicas:

* `POST /v1/usuarios/{usuario_id}/ativar`
* `POST /v1/usuarios/{usuario_id}/resetar-senha`

Query params:

* `GET /v1/usuarios?ativo=true&page=1&limit=20`

---

### Produtos

* `GET    /v1/produtos` → lista produtos
* `POST   /v1/produtos` → cria produto
* `GET    /v1/produtos/{produto_id}` → detalhe
* `PUT    /v1/produtos/{produto_id}` → atualiza totalmente
* `PATCH  /v1/produtos/{produto_id}` → atualiza parcialmente
* `DELETE /v1/produtos/{produto_id}` → deleta

Filtros e ordenação:

* `GET /v1/produtos?categoria=eletronicos&disponivel=true`
* `GET /v1/produtos?sort=-preco&page=2&limit=50`

---

### Pedidos

Relacionados a usuários:

* `GET    /v1/usuarios/{usuario_id}/pedidos` → pedidos do usuário
* `POST   /v1/usuarios/{usuario_id}/pedidos` → cria pedido para usuário

Rotas diretas (quando você já sabe o ID do pedido):

* `GET    /v1/pedidos/{pedido_id}` → detalhe do pedido
* `PATCH  /v1/pedidos/{pedido_id}` → atualiza status, etc.
* `DELETE /v1/pedidos/{pedido_id}` → cancela/exclui

Ação de negócio:

* `POST /v1/pedidos/{pedido_id}/cancelar`

Filtros:

* `GET /v1/pedidos?status=aberto`
* `GET /v1/pedidos?data_inicio=2025-01-01&data_fim=2025-01-31`

---

### Autenticação (exemplo simples)

Mesmo que em produção isso fique mais elaborado, algo como:

* `POST /v1/auth/login` → recebe `{ "email": "...", "senha": "..." }` e devolve token
* `POST /v1/auth/refresh` → renova token

---

Essa estrutura já é suficiente para você:

* mapear recursos;
* usar verbos HTTP corretamente;
* trabalhar com hierarquia;
* incluir versionamento;
* ter padrão para erros e query params.

Quando trouxermos isso para FastAPI, basicamente vamos transformar esses endpoints em funções Python decoradas (`@app.get`, `@app.post`, etc.), com modelos Pydantic para validação de entrada/saída. A mágica é que, se a “arquitetura de rotas” estiver bem pensada, o código acompanha e continua limpo.
