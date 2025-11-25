# Primeiros Passos com Git e Github

Vamos dar forma ao seu primeiro passeio prático com Git e GitHub. Aqui a ideia é mostrar não só os comandos, mas o **raciocínio por trás de cada ação**, porque Git é muito mais sobre fluxo mental do que memorização mecânica. Com esses passos, você já navega pelo versionamento com a naturalidade de quem sabe o que está acontecendo debaixo do capô.

---

# **Criar e Clonar Repositórios**

## **Criar um repositório novo (local)**

Quando você tem uma pasta e quer transformá-la em um repositório:

```bash
git init
```

Isso cria a “câmara do tempo” do Git dentro da pasta (`.git`), e a partir daí tudo que você versiona ganha histórico.

Verifica o estado inicial:

```bash
git status
```

## **Criar um repositório no GitHub**

No GitHub:

**New Repository → nome, descrição, Create Repository**

Você receberá instruções do tipo:

```bash
git remote add origin https://github.com/usuario/repositorio.git
git branch -M main
git push -u origin main
```

Esse conjunto de comandos conecta seu repositório local ao remoto.

## **Clonar um repositório existente**

Para trazer um projeto já existente do GitHub para sua máquina:

```bash
git clone https://github.com/usuario/repositorio.git
```

Esse comando:

1. baixa o repositório
2. cria uma pasta com o conteúdo
3. configura o remoto automaticamente

Clonar é a maneira mais limpa de começar num projeto já sincronizado.

---

# **Salvar alterações no repositório local**

O fluxo é sempre o mesmo — três passos que viram quase uma coreografia:

### **1. Ver o que mudou**

```bash
git status
```

### **2. Preparar arquivos para o commit**

```bash
git add arquivo.py
```

Ou tudo:

```bash
git add .
```

### **3. Criar o commit**

```bash
git commit -m "Mensagem explicando o que mudou"
```

Um commit é um ponto no tempo: um checkpoint.
Cada um deve capturar uma mudança lógica, não um “lote aleatório”.

---

# **Desfazer alterações no repositório local**

Git é uma máquina do tempo: dá pra voltar atrás sem medo.

## **Desfazer alterações ainda não adicionadas (não estão no stage)**

```bash
git restore arquivo.py
```

Volta o arquivo ao estado do último commit.

## **Desfazer arquivos que já estão no stage**

```bash
git restore --staged arquivo.py
```

Sai da área de staging, mas mantém seu conteúdo no disco.

## **Voltar ao estado de um commit anterior**

```bash
git checkout -- arquivo.py
```

Ou, para voltar o repositório inteiro:

```bash
git reset --hard HEAD~1
```

Esse apaga mesmo — use só quando tiver certeza.

O ponto é que Git permite ajustar erros sem pânico.

---

# **Enviar e baixar alterações do repositório remoto**

## **Enviar commits para o GitHub**

```bash
git push
```

Se for a primeira vez, pode precisar definir:

```bash
git push -u origin main
```

O `-u` cria o vínculo, e depois só `git push` funciona.

## **Baixar mudanças do remoto**

```bash
git pull
```

Esse comando faz dois movimentos:

1. baixa as alterações (`fetch`)
2. mescla com o seu trabalho local (`merge`)

Se quiser ver sem mesclar:

```bash
git fetch
```

Isso te deixa analisar as diferenças antes de integrar.

---

# **Trabalhar com branches: criar, mesclar, deletar, lidar com conflitos**

Branches são trilhas paralelas da história.
Você cria uma linha alternativa, trabalha nela e depois integra.

### **Criar um novo branch**

```bash
git checkout -b nova-ideia
```

Ou em duas etapas:

```bash
git branch nova-ideia
git checkout nova-ideia
```

Agora você está em um universo paralelo onde pode alterar tudo sem mexer na `main`.

### **Mesclar alterações de volta à main**

Primeiro volte para a main:

```bash
git checkout main
```

Mescle:

```bash
git merge nova-ideia
```

Se tudo encaixar, o merge é automático.

### **Apagar um branch após o merge**

```bash
git branch -d nova-ideia
```

Ou forçar (caso não tenha merge):

```bash
git branch -D nova-ideia
```

### **Quando ocorre conflito**

Se duas pessoas (ou dois branches) alteram a mesma parte do mesmo arquivo, Git pede ajuda.

O arquivo fica assim:

```
<<<<<< HEAD
linha da main
======
linha do branch
>>>>>> nova-ideia
```

Você resolve manualmente:

* escolhe uma,
* mistura as duas,
* ou reescreve tudo.

Depois:

```bash
git add arquivo
git commit
```

Conflitos são normais — fazem parte do fluxo colaborativo.

---

# **Branches: comandos úteis no dia a dia**

Aqui estão os comandos que realmente entram na rotina de quem usa Git todos os dias:

### **Listar branches**

```bash
git branch
```

### **Ver branches remotos e locais**

```bash
git branch -a
```

### **Trocar de branch**

```bash
git checkout nome-do-branch
```

Novo estilo (mais moderno):

```bash
git switch nome-do-branch
```

### **Criar branch com switch**

```bash
git switch -c nova-funcionalidade
```

### **Ver últimos commits em formato visual**

```bash
git log --oneline --graph --decorate --all
```

Parece até uma árvore genealógica do seu código.

### **Atualizar seu branch com a main**

```bash
git checkout nova-ideia
git merge main
```

Ou com rebase, que deixa a história mais linear:

```bash
git rebase main
```

*(Rebase é maravilhoso, mas exige respeito. A gente fala disso quando quiser.)*

---

# **Amarrando tudo**

Nesse ponto você já vê o Git não como uma caixa-preta, mas como um sistema lógico:

• criar e clonar te situam no começo
• commit é seu passo narrativo
• push/pull sincronizam mundos
• branches criam universos paralelos
• merges aproximam esses universos
• conflitos são apenas partes que precisam de tradução humana

Com isso em mãos, você já consegue trabalhar em qualquer projeto, sozinho ou em equipe, com clareza e segurança.
