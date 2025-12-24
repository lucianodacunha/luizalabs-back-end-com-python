# **Bases de Prompt Engineering para o GitHub Copilot**

Aqui a chave vira de verdade. Até agora, o Copilot foi “útil”. A partir daqui, ele passa a ser **dirigível**. Prompt engineering não é mágica nem truque — é **comunicação precisa com um sistema probabilístico**. Quem entende isso deixa de reagir às sugestões e passa a **orquestrá-las**.

---

## 1️⃣ Uso clássico do Copilot: comentário → código

### Introdução

O uso mais comum (e mais subestimado) do **GitHub Copilot** é simples:

> escrever um comentário e deixar o Copilot completar o código.

Isso parece trivial, mas é exatamente aqui que o *prompt engineering* começa.

---

### O que é Prompt Engineering (sem misticismo)

Prompt engineering é a prática de **formular instruções de forma que aumentem a probabilidade** da IA gerar algo útil.

Não é comando determinístico.
É **direcionamento estatístico**.

Você não diz:

> “faça exatamente isso”

Você diz:

> “é isso que estou tentando fazer, neste contexto”

E a IA tenta o caminho mais provável.

---

### Learning shots (ou: ensinar pelo exemplo)

Um conceito central é o de *shots* — exemplos que ensinam o padrão.

No Copilot, isso acontece **implicitamente**:

* nomes de funções;
* código existente no arquivo;
* estilo já usado;
* comentários anteriores.

Exemplo simples:

```python
# cria um endpoint FastAPI para listar usuários ativos
```

Se, logo acima, já existe um endpoint parecido, o Copilot “aprende” o padrão e replica.

Isso é **few-shot learning na prática**, sem você perceber.

---

### Aplicando prompt engineering em comentários

Compare estes dois comentários:

**Vago**

```python
# endpoint de usuário
```

**Direcionado**

```python
# endpoint FastAPI para listar usuários ativos com paginação (page, limit)
```

O segundo:

* define tecnologia;
* define ação;
* define regras;
* define parâmetros.

Resultado: sugestões muito mais próximas do que você quer.

Regra de ouro:

> **comentários são prompts disfarçados**

---

### Copilot inline: transformar código já existente

Prompt engineering não serve só para gerar código do zero.

Você pode **guiar refatorações**.

Exemplo:

```python
# refatorar esta função para async, usando SQLAlchemy AsyncSession
def listar_usuarios():
    ...
```

O Copilot usa:

* o código existente;
* o comentário;
* o contexto do projeto.

E tenta gerar a versão assíncrona.

Aqui, você não aceita tudo — você **negocia com a sugestão**.

---

## 2️⃣ Compreendendo prompt engineering e mudando a geração

Agora entramos no nível conceitual que muda sua postura mental.

---

### AI, estocástica e xLMs (o que realmente está acontecendo)

Modelos como o Copilot são **xLMs (cross-domain Language Models)**:

* treinados em texto e código;
* operam por **probabilidade condicional**;
* geram o próximo token mais provável dado o contexto.

Importante:

* eles **não sabem** se algo está certo;
* eles **não entendem intenção**, só padrões;
* eles **não têm memória de longo prazo** fora do contexto atual.

Tudo é estatística orientada por contexto.

---

### Por que as respostas variam?

Porque o processo é **estocástico**:

* pequenas mudanças no prompt mudam a distribuição de probabilidade;
* mudar uma palavra muda o “caminho” da geração.

Exemplo:

```python
# criar função
```

vs

```python
# criar função pura, sem efeitos colaterais, para cálculo determinístico
```

O segundo restringe muito mais o espaço de geração.

---

### Hora de controlar essas gerações

Controlar o Copilot não é “mandar”, é **limitar o espaço de resposta**.

Você faz isso com:

1. **Contexto explícito**

   ```python
   # usando SQLAlchemy ORM async
   ```

2. **Restrições**

   ```python
   # sem acessar banco diretamente
   ```

3. **Estilo**

   ```python
   # seguindo padrão do módulo usuarios
   ```

4. **Objetivo claro**

   ```python
   # retornar apenas dados públicos do usuário
   ```

Quanto mais você restringe, menos o Copilot “viaja”.

---

### Mudando a geração sem brigar com ela

Se a sugestão veio errada, não lute com ela. **Re-prompt**.

Exemplo:

```python
# versão anterior está síncrona, reescrever como async usando await
```

Ou:

```python
# evitar loops, usar compreensão de lista
```

Você está **editando o prompt**, não corrigindo a IA à força.

---

## A leitura madura do Prompt Engineering no Copilot

Prompt engineering não é:

* decorar frases mágicas;
* confiar cegamente;
* terceirizar pensamento.

É:

* comunicar intenção;
* reduzir ambiguidade;
* moldar probabilidade.

Quem entende isso:

* escreve menos;
* revisa mais;
* pensa em nível mais alto.

Quem não entende:

* aceita sugestões ruins;
* cria bugs elegantes;
* culpa a ferramenta.

O **GitHub** Copilot é um amplificador.
Amplificadores aumentam tanto o bom quanto o ruim.

Com prompt engineering consciente, você não “usa IA”.
Você **dirige um sistema probabilístico** para trabalhar a seu favor — com método, critério e controle.
