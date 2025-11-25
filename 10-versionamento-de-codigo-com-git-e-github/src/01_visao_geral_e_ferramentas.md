# Visão Geral e Ferramentas

Versionamento é uma dessas tecnologias que parece simples à primeira vista — “guardar versões” — mas que, quando você entende o espírito da coisa, vira praticamente uma máquina do tempo para o seu código. E Git e GitHub são as ferramentas que tornaram isso acessível ao mundo inteiro, do estudante ao CERN.

---

## **Introdução**

Programar é lidar com mudança: ideias mudam, requisitos mudam, arquivos mudam. E, se você só salvar por cima ou criar pastas tipo “projeto_final_v3_agora_vai”, eventualmente a situação vira um labirinto inglório.

Versionamento de código resolve esse caos desde a raiz. Ele registra as transformações no código ao longo do tempo e te permite voltar, comparar, experimentar, ramificar e colaborar sem medo.

É como transformar o seu projeto em uma história — cada commit é um capítulo, cada branch é um universo paralelo, e você pode viajar entre eles quando quiser.

---

## **O que é versionamento de código**

É o processo de **registrar, organizar e controlar mudanças** em arquivos — especialmente códigos-fonte — ao longo do tempo.

Com versionamento, você pode:

• saber o que mudou
• saber *quando* mudou
• saber *quem* mudou
• voltar para qualquer estado anterior
• trabalhar em equipe sem sobrescrever o trabalho do outro

Versionamento é essencialmente **controle + histórico + colaboração**.

A imagem mental:
Seu projeto vira uma timeline com checkpoints.
Cada checkpoint é um commit.
E você pode voltar a qualquer um deles como se estivesse assistindo uma gravação.

---

## **O que é Git**

Git é um sistema de controle de versão criado por Linus Torvalds.
Ele funciona de forma distribuída, o que significa:

* cada máquina tem **o repositório completo** (não só uma cópia)
* sem internet, tudo funciona igual
* histórico, branches e merges são locais

O Git resolveu problemas que sistemas anteriores tinham, e trouxe uma série de vantagens:

### **1. Velocidade**

Quase tudo é instantâneo.

### **2. Segurança**

Cada commit é identificado por um hash criptográfico.

### **3. Branches leves e rápidos**

Criar um branch é como criar uma nova trilha narrativa do projeto — sem sofrimento, sem peso, sem risco.

```bash
git branch nova-ideia
git checkout nova-ideia
```

### **4. Controle absoluto**

Você decide o que entra no commit, como organiza, como volta atrás, como mescla.

### **5. Funcionamento 100% local**

Você pode versionar projetos inteiros sem tocar na internet.

Git é uma ferramenta de poder e precisão. No começo parece misteriosa, mas com prática vira extensão do pensamento.

---

## **O que é GitHub**

Se Git é o motor, GitHub é a cidade onde os repositórios vivem.

GitHub é uma plataforma online que:

* armazena repositórios Git
* facilita colaboração
* automatiza processos
* oferece recursos visuais e sociais

Ele transforma o fluxo Git em algo acessível e conectado.

### Principais funções do GitHub:

**1. Hospedar repositórios remotos**
Seu código fica disponível, seguro e sincronizado.

```bash
git push origin main
```

**2. Colaboração estruturada**
• Pull Requests
• Issues
• Code Reviews

Essas ferramentas criam um fluxo profissional de desenvolvimento, mesmo para projetos solo.

**3. GitHub Pages**
Hospeda sites diretamente do repositório — útil para documentação, portfolios, projetos estáticos.

**4. GitHub Actions**
Automação: testes, deploy, pipelines — tudo integrado ao versionamento.

**5. Social coding**
Estrelas, forks, organização por equipes, descoberta de projetos, ecossistema gigantesco.

GitHub virou praticamente a rede social dos desenvolvedores — mas voltada para construção real, não só conversa.

---

## **Amarrando tudo**

• **Versionamento** é a arte de acompanhar e controlar mudanças.
• **Git** é a ferramenta que permite isso de forma rápida, segura e distribuída.
• **GitHub** é a plataforma que dá colaboração, visibilidade e automação ao Git.

Git cuida da sua história.
GitHub cuida das pessoas que trabalham nessa história.
