# Exemplos Práticos

---

# **1. Pull Requests e fluxo colaborativo — exemplo completo**

### **Você quer criar uma nova funcionalidade chamada “login”**

```bash
# criar o branch da funcionalidade
git switch -c feature-login

# editar arquivos, criar a funcionalidade
git add .
git commit -m "feat: adiciona tela de login"
```

### **Enviar o branch para o GitHub**

```bash
git push -u origin feature-login
```

### **No GitHub**

1. Vai aparecer um banner: *"Compare & Pull Request"*
2. Você abre o PR
3. Adiciona descrição
4. Revisor comenta, aprova
5. Aperta **Merge**

Depois do merge, você pode deletar o branch no GitHub (ou no terminal):

```bash
git branch -d feature-login
```

Esse é o ciclo básico de colaboração.

---

# **2. stash, rebase e cherry-pick — uso real**

## **A. stash — guardando mudanças do nada**

Você está modificando um arquivo quando recebe uma tarefa urgente:

```bash
git status
# você vê que tem alterações não commitadas

git stash
# tudo some da pasta (mas está guardado)
```

Troca de branch sem culpa:

```bash
git switch main
```

Quando quiser recuperar:

```bash
git stash pop
```

Pronto — seu trabalho recuperado.

---

## **B. rebase — colocando seu branch no topo da main**

Você criou um branch “feature-x”.
Enquanto trabalhava, a `main` recebeu novos commits.

Atualizar seu branch:

```bash
git switch feature-x
git fetch origin
git rebase origin/main
```

Se houver conflitos, o Git pausa e você resolve manualmente.
Depois continua:

```bash
git add arquivo
git rebase --continue
```

O resultado é uma história **linear e limpa**.

---

## **C. cherry-pick — copiando commits específicos**

Você cometeu um “fix” no branch errado:

```bash
git log --oneline
# encontrou o hash: a1b2c3d
```

Quer aplicar esse fix em outro branch:

```bash
git switch main
git cherry-pick a1b2c3d
```

Isso cria o mesmo commit na `main`.
É como puxar exatamente o que você quer, sem trazer bagagem extra.

---

# **3. Git Avançado: tags, releases, bisect**

## **A. Criando tags para marcar versões**

```bash
git tag v1.0.0
git push origin v1.0.0
```

No GitHub → aparece em "Releases and Tags”.

Criar tag anotada (com mensagem):

```bash
git tag -a v1.0.0 -m "Primeira versão estável"
```

---

## **B. Criando uma release no GitHub**

1. Vá em **Releases → Draft a new release**
2. Escolha a tag v1.0.0
3. Adicione notas
4. Publique

Isso organiza marcos do projeto com clareza profissional.

---

## **C. bisect — encontrar o commit que introduziu o bug**

Situação: algo que funcionava quebrou “em algum commit”.

```bash
git bisect start
git bisect bad          # estado atual (bugado)
git bisect good abc123  # commit antigo que você sabe que estava bom
```

Git te leva para um commit intermediário.
Você testa:

```bash
python sistema.py
```

Se o bug aparece:

```bash
git bisect bad
```

Se não:

```bash
git bisect good
```

Git repete o processo até achar o commit exato.

Finaliza:

```bash
git bisect reset
```

É um detector cirúrgico de bugs.

---

# **4. Fluxos de Trabalho: GitFlow e Trunk-based — exemplos**

## **A. GitFlow — como fica na prática**

### Branches principais:

* `main`
* `develop`

### Criar uma feature:

```bash
git switch develop
git switch -c feature/pagamento
```

Depois:

```bash
git add .
git commit -m "feat: módulo pagamento"
git push origin feature/pagamento
```

Merge para `develop` via PR.

### Criar uma release:

```bash
git switch develop
git switch -c release/1.2.0
```

Testa, ajusta, depois:

* merge em `main`
* merge em `develop`

### Hotfix:

```bash
git switch main
git switch -c hotfix/corrige-login
```

Corrige, merge para:

* `main`
* `develop`

GitFlow cria uma dança organizada entre vários tipos de branch.

---

## **B. Trunk-based development — como fica**

É muito mais simples:

* Tudo gira em torno da `main`.
* Branches curtíssimos, geralmente 1 dia ou menos.
* Feature flags para código incompleto.

Criar branch:

```bash
git switch -c botao-dark-mode
```

Trabalhar rapidamente:

```bash
git add .
git commit -m "feat: cria botão dark mode (desativado por flag)"
git push
```

PR pequeno → merge rápido.
Nada de branches longos.
História sempre limpa.

É o modelo usado por empresas que fazem deploy contínuo.
