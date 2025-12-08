### Introdução ao desenvolvimento web

Desenvolver para a web é criar sistemas que vivem dentro de um ecossistema distribuído. Quando alguém usa um app, abre um navegador ou dispara uma integração entre serviços, existe uma coreografia acontecendo entre cliente, servidor e rede.

O navegador é só a ponta visível de um iceberg lógico gigantesco. O servidor, por sua vez, é como um estúdio de cinema: recebe pedidos, processa dados, consulta banco, roda regras de negócio e devolve algo útil. A web inteira é mediada por protocolos — acordos formais que garantem que máquinas diferentes conversem sem precisar discutir sotaques.

---

### Como a web funciona

A web roda sobre o protocolo HTTP, um acordo simples: o cliente pede, o servidor responde. Isso lembra uma conversa telegráfica.

Quando você acessa `https://meusite.com/produtos/1`, o navegador monta uma requisição HTTP contendo método, cabeçalhos e, às vezes, corpo. A requisição atravessa a rede, chega ao servidor, que roda alguma lógica e devolve uma resposta contendo código de status (200, 404, 500…), cabeçalhos e um corpo — normalmente JSON ou HTML.

Esse ciclo se repete milhões de vezes por minuto mundo afora, como um gigantesco formigueiro digital coordenado por pacotes TCP/IP.

---

### Tecnologias front-end e back-end

Front-end é a vitrine, back-end é o estoque.
No front, vive HTML (estrutura), CSS (estilo) e JavaScript (interatividade). Frameworks como React, Vue e Angular tornam isso mais poderoso.

No back-end, vive o cérebro: Python, Java, Node.js, Go, etc. É nele que ficam autenticação, regras de negócio, acesso ao banco de dados e lógica da API.

Imagine uma aplicação de vendas: o front mostra o botão “Comprar”, o back decide o que acontece quando o botão é pressionado.

---

### API e conceitos fundamentais

API significa “Application Programming Interface” — uma interface para que sistemas conversem entre si.

Uma API web expõe *endpoints*, que são URLs que respondem a métodos HTTP. Elas operam como portas numeradas em um hotel: cada uma serve a um propósito.

Conceitos essenciais:
- Endpoint: URL que representa um recurso (ex.: `/usuarios/42`).
- Recurso: entidade do sistema (usuários, produtos, pedidos etc.).
- Representação: forma como enviamos ou recebemos dados (JSON, XML…).
- Stateless: a requisição não depende de memória do servidor entre chamadas — cada pedido carrega seu próprio contexto.
- Autenticação e autorização: quem você é e o que pode fazer.
- Versionamento: modificar sem quebrar quem já usa (ex.: `/v1/produtos`).

APIs são a espinha dorsal da comunicação entre serviços modernos, e FastAPI nasceu exatamente para torná-las rápidas, seguras e elegantes.

---

### Tipos de APIs: RESTful, SOAP e GraphQL

**RESTful**
REST é um estilo arquitetural baseado em recursos e verbos HTTP.
Ele usa URLs simples, respostas em JSON e operações padronizadas.
É pragmático, leve e adotado globalmente — o arroz com feijão da web moderna.

**SOAP**
Uma criatura de outra era. Baseia-se em XML, contratos muito rígidos e camadas de segurança formais. É comum em sistemas bancários e corporativos mais antigos. Funciona bem, mas é burocrático como um cartório.

**GraphQL**
Uma abordagem mais flexível: o cliente diz exatamente quais dados quer. É ótimo quando o front tem necessidades complexas ou variáveis. Em compensação, o servidor precisa ser mais inteligente. É quase uma API que pensa em "consultas" como se fosse um banco estruturado para consumo externo.

---

### Verbos HTTP: GET, POST, PUT, PATCH, DELETE

Esses verbos são a gramática das APIs REST.

**GET**
Pede dados. Sem efeitos colaterais. Ex.: listar produtos.

**POST**
Cria algo novo. Ex.: cadastrar um usuário.

**PUT**
Substitui um recurso inteiro. Se o recurso tem três campos e você manda só dois, o terceiro deve ser sobrescrito como vazio. É a reforma completa.

**PATCH**
Atualiza parcialmente. Só altera os campos enviados. Ajuste fino.

**DELETE**
Remove um recurso. Adeus, registro.
