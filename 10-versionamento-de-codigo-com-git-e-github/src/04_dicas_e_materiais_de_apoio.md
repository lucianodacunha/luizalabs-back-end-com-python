# Dicas e Materiais de Apoio

Vamos abrir as portas de um nível acima no mundo Git/GitHub — onde colaboração, organização e engenharia de código começam a ganhar textura profissional. Esses tópicos fazem parte do repertório cotidiano de equipes grandes, projetos open-source e pipelines mais sérios.

A boa notícia: cada um deles, quando entendido, remove um pouco daquela “aura de complexidade” que às vezes cerca o Git. Eles são mais conceituais do que difíceis.

---

# **Pull Requests e fluxo colaborativo no GitHub**

Um Pull Request (PR) é uma conversa formal sobre uma mudança de código.
Você cria um branch, faz seus commits, envia para o GitHub e abre um PR pedindo:

> “Pessoal, podem revisar e integrar essa mudança?”

### **Fluxo geral**

1. Criar branch:

   ```bash
   git switch -c nova-funcionalidade
   ```
2. Fazer commits normalmente
3. Enviar o branch:

   ```bash
   git push -u origin nova-funcionalidade
   ```
4. No GitHub → **New Pull Request**
5. Revisão, comentários, sugestões
6. Merge quando tudo estiver aprovado
7. Branch pode ser deletado

### **Por que PR é poderoso?**

* revisão por pares (qualidade)
* histórico limpo
* discussão centralizada
* automações (testes, lint, deploy) com GitHub Actions
* segurança (proteger a `main` contra pushes diretos)

Um PR é como uma “carta de intenção” do seu código, antes de ele entrar na história principal.

---

# **Versionamento sem medo: stash, rebase, cherry-pick**

Aqui entramos em ferramentas que parecem avançadas, mas fazem o dia a dia fluir com mais suavidade.

---

## **stash — guardar mudanças temporariamente**

Quando você está no meio de algo, mas precisa trocar de branch:

```bash
git stash
```

Suas mudanças somem da pasta (mas ficam guardadas).
Para restaurá-las:

```bash
git stash pop
```

É um bolso secreto: útil, seguro e rápido.

---

## **rebase — organizar a história**

Rebase permite “recontar” a história colocando seus commits em cima da versão mais recente da `main` (ou outro branch).

Imagine:

* Você criou o branch `feature-x`
* A `main` avançou com novos commits
* Rebase atualiza sua linha:

```bash
git checkout feature-x
git rebase main
```

Sua história fica linear, como se o seu trabalho sempre tivesse começado na última versão da `main`.
Em PRs, isso deixa tudo mais elegante.

### **Regra de ouro:**

Use rebase **somente** em branches pessoais (não compartilhados).
Nunca rebases commits já publicados sem coordenação.

---

## **cherry-pick — trazer commits específicos**

Você quer pegar apenas um commit de outro branch.
Git permite:

```bash
git cherry-pick <hash>
```

Isso copia o commit (não o branch inteiro) para onde você está.
É útil quando:

* um fix feito em `dev` precisa ir para `main` rapidamente
* você quer isolar commits de teste
* precisa “salvar” uma mudança feita no branch errado

Cherry-pick é bisturi: preciso e direto.

---

# **Git avançado: tags, releases, bisect**

Essas ferramentas são a camada de engenharia do Git — úteis quando você quer organizar versões, diagnosticar bugs ou fazer lançamentos formais.

---

## **tags — marcar pontos importantes**

Uma tag é um marcador permanente no histórico.

```bash
git tag v1.0.0
git push origin v1.0.0
```

Elas servem para:

* versões do software
* marcos importantes (“final do módulo”)
* checkpoints confiáveis

GitHub usa tags para gerar **releases** automaticamente.

---

## **releases — pacotes oficiais**

No GitHub, uma release é:

* uma tag
* * notas de versão
* * artefatos anexados (se houver)
* * histórico de mudanças

É como publicar um capítulo finalizado do projeto para o mundo.

---

## **bisect — encontrar o commit que introduziu um bug**

É quase um detector de falhas baseado em busca binária.

Fluxo:

```bash
git bisect start
git bisect bad        # commit onde o bug existe
git bisect good <hash-antigo>
```

Git passa a te mover por commits intermediários.
Você testa, diz “good” ou “bad”, e ele reduz o intervalo.
No final, aponta o commit culpado.

É uma ferramenta incrível para detetives de bugs.

---

# **Fluxos de trabalho modernos: GitFlow e Trunk-based Development**

Agora entramos na filosofia de organização.

---

## **GitFlow — o modelo clássico de ramificação**

Perfeito para projetos grandes, planejados, com ciclos de release definidos.

Ele define:

* `main` = releases estáveis
* `develop` = linha principal de desenvolvimento
* branches auxiliares:

  * `feature/*`
  * `release/*`
  * `hotfix/*`

Fluxo:

1. Criar feature em `feature/nome`
2. Mesclar em `develop`
3. Quando pronto para release → `release/x.y.z`
4. Mescla em `main` e `develop`
5. Hotfixes vão direto de `main` para `develop`

É estruturado, robusto, mas pode ser pesado para equipes pequenas.

---

## **Trunk-based Development — o modelo moderno e leve**

Cada vez mais adotado em empresas que prezam velocidade, integração contínua e deploy frequente.

Princípios:

* `main` é sempre estável
* branches são curtos e vivem pouco
* PRs pequenos
* integrações frequentes
* feature flags para código incompleto

Equipes Google, Meta, Uber e cia usam variações disso.

GitFlow é como uma máquina com várias engrenagens.
Trunk-based é como uma corrente simples e eficiente.

---

# **Amarrando tudo**

Esses tópicos te levam para o Git “de verdade” — onde colaboradores conversam, branches surgem e desaparecem, histórias são reorganizadas e bugs são rastreados pela timeline do projeto.

• **Pull Requests** organizam colaboração.
• **Stash, rebase e cherry-pick** dão fluidez ao fluxo pessoal.
• **Tags, releases e bisect** trazem maturidade.
• **GitFlow e Trunk-based** te ajudam a escolher um estilo de trabalho.
