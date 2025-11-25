# Instalação, Configuração e Autenticação

Instalar e configurar o Git é quase um ritual de iniciação no mundo do versionamento: alguns comandos, um pouco de identidade digital e, de repente, você ganha superpoderes para controlar o tempo e colaborar com outras mentes. Vamos destrinchar isso com clareza e ritmo leve.

---

## **Instalação**

O Git funciona em qualquer sistema operacional, e a instalação é sempre direta.

### **No Windows**

A opção clássica é baixar o instalador no site oficial:

```
https://git-scm.com
```

O instalador inclui:

* o Git em si
* o Git Bash (um terminal muito prático)
* integração com o Explorer

Depois da instalação, abra o **Git Bash** e você já está no jogo.

### **No Ubuntu / Linux**

O próprio sistema embala o Git:

```bash
sudo apt update
sudo apt install git
```

Simples e direto.

### **No macOS**

Se digitar `git` no terminal, o sistema oferece instalar automaticamente os *Command Line Tools*.
Ou você instala via Homebrew:

```bash
brew install git
```

No fim, todos esses caminhos levam ao mesmo executável limpo e poderoso.

---

## **Configuração**

Depois da instalação, o Git ainda não sabe *quem é você*.
E isso importa, porque cada commit carrega sua assinatura — não para controlar, mas para contar a história corretamente.

### **Configuração global de identidade**

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

Essas duas linhas fazem o Git te reconhecer como autor dos commits.

### **Ver suas configurações**

```bash
git config --list
```

### **Escolha do editor**

O Git abre mensagens de commit e merges em um editor.
Se você usa VSCode:

```bash
git config --global core.editor "code --wait"
```

Isso muda a experiência completamente — editar mensagens no VSCode é bem mais agradável do que no editor padrão.

### **Padrões úteis**

Mostrar cores nos comandos:

```bash
git config --global color.ui auto
```

Ignorar arquivos temporários no mundo inteiro:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

Você cria o arquivo:

```bash
# exemplo de conteúdo
.DS_Store
Thumbs.db
```

E ele vale para todos os repositórios.

---

## **Autenticação**

Aqui entramos no coração digital da coisa: **como provar ao GitHub (ou GitLab, Bitbucket, etc.) que você é você**.

Antigamente usávamos senha.
Hoje, por segurança, o GitHub só aceita:

* tokens pessoais (PAT)
* chaves SSH
* GitHub CLI

Vamos ver cada uma.

---

## **1. Autenticação via Token (PAT)**

É o método mais simples para começar.
O GitHub gera um token — uma espécie de “senha de uso único estendida”.

Caminho no GitHub:

**Settings → Developer Settings → Personal Access Tokens → Tokens (classic)**

Crie um token com permissões:

* repo
* gist
* user (opcional)

Ao fazer `git push`, o Git pede “senha”.
Você cola o token — e pronto.

No VSCode, ele armazena no gerenciador de credenciais do sistema.

---

## **2. Autenticação via SSH**

É o método preferido por muita gente: rápido, seguro e elegante.

Crie uma chave no seu computador:

```bash
ssh-keygen -t ed25519 -C "seuemail@example.com"
```

Ela fica em:

```
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

Você pega o conteúdo do arquivo `.pub` e adiciona no GitHub:

**Settings → SSH and GPG keys → New SSH key**

Depois disso, pode clonar assim:

```bash
git clone git@github.com:usuario/repositorio.git
```

E `push/pull` funcionam sem pedir senha.

---

## **3. GitHub CLI (gh)**

Uma ferramenta de linha de comando que facilita logins e operações.

Instalação (Ubuntu):

```bash
sudo apt install gh
```

Login:

```bash
gh auth login
```

É quase conversar com uma assistente — simples e direto.

---

## **Testando tudo**

Depois de configurar e autenticar, teste:

```bash
git clone git@github.com:usuario/repositorio.git
```

ou

```bash
git clone https://github.com/usuario/repositorio.git
```

Clone um repositório, faça um commit simples e envie:

```bash
git add .
git commit -m "Teste"
git push
```

Se funcionou sem dor, sua configuração está alinhada.

---

## **Amarrando tudo**

• Instalação dá a ferramenta.
• Configuração dá identidade.
• Autenticação dá acesso ao repositório remoto.

A partir daí, o Git vira seu diário, e o GitHub vira sua vitrine — tudo conectado, seguro e fluido.
