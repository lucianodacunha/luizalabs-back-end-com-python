# Ambiente de desenvolvimento e primeiros passos com Python

## Notas

1. Conceito rápido: o que são “virtualização de ambiente” e “gerenciadores”
2. Explicar pyenv, venv/virtualenv, conda/Anaconda
3. Citar mais 1–2 opções que valem conhecer
4. Recomendações práticas para Ubuntu e Windows

---

## 1. Antes de tudo: separar dois problemas diferentes

Quando a gente fala “virtualização de ambiente” em Python, na prática está misturando dois tipos de ferramenta:

1. **Gerenciador de versões de Python**

   * Ex.: `pyenv`
   * Resolve: “quero ter Python 3.10, 3.11 e 3.12 na mesma máquina e escolher qual usar por projeto.”

2. **Gerenciador de ambientes / dependências**

   * Ex.: `venv`, `virtualenv`, `conda`, `poetry`, `pipenv`
   * Resolve: “neste projeto quero `geopandas==0.14`, no outro `geopandas==0.13` sem um quebrar o outro.”

Muita confusão some quando você separa essas duas caixinhas na cabeça.

---

## 2. pyenv

**O que é:**
Ferramenta para instalar e alternar entre múltiplas versões de Python na mesma máquina.

**Pontos fortes:**

* Instala várias versões de Python lado a lado (3.8, 3.9, 3.10, 3.11, etc.).
* Permite definir:

  * versão global (`pyenv global 3.11.6`)
  * versão por diretório/projeto (`pyenv local 3.10.13` → cria `.python-version`)
* Integra bem com `venv`, `virtualenv`, `poetry` etc.

**Onde brilha:**

* Em **Linux/macOS (Ubuntu incluso)** é excelente.
* Em **Windows**, existe o *pyenv-win*, que funciona, mas não é tão redondo quanto no Linux. Ainda assim, é uma opção.

**Fluxo típico com pyenv no Ubuntu:**

```bash
pyenv install 3.11.6
pyenv local 3.11.6          # nesse projeto
python -m venv .venv        # cria ambiente
source .venv/bin/activate   # ativa
pip install geopandas
```

---

## 3. venv e virtualenv

### venv (módulo padrão)

**O que é:**
Módulo da própria stdlib do Python (desde 3.3) para criar ambientes virtuais.

* Comando clássico:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate
```

**Vantagens:**

* Já vem com o Python, nada extra pra instalar.
* Simples, funciona bem para a maioria dos casos.
* Ótimo para projetos simples a médios.

### virtualenv

**O que é:**
Ferramenta mais antiga, que inspirou o `venv`. Ainda é usada, principalmente por ter alguns recursos extras e ser um pouco mais rápida/flexível em certos cenários.

```bash
pip install virtualenv
virtualenv .venv
```

**Hoje, em 2025:**
Para a maioria dos casos, **`venv` resolve bem**. `virtualenv` é útil quando você quer recursos específicos ou tem legado.

---

## 4. Conda e Anaconda

Aqui entra o mundo “baterias incluídas”.

### conda (Miniconda / Anaconda / Mambaforge)

**O que é:**
Gerenciador de **ambientes** e **pacotes** que não é limitado só a Python. Ele instala também binários nativos (GDAL, PROJ, QGIS, etc.), o que é ouro para geoprocessamento.

**Características:**

* Cria ambientes isolados:

```bash
conda create -n geo python=3.11
conda activate geo
conda install geopandas gdal
```

* Consegue instalar libs difíceis (GDAL, rasterio, etc.) sem você sofrer com compilação.
* Usa *channels* (canais de pacotes), o mais famoso pra ciência/geospatial é o `conda-forge`.

### Anaconda vs Miniconda

* **Anaconda**: distribuição “com tudo dentro” (milhares de pacotes instalados por padrão).

  * Bom pra quem quer um ambiente de data science pronto.
  * Pesado, ocupa bastante espaço.

* **Miniconda / Mambaforge**:

  * Instala só o básico (Python + conda).
  * Você instala o que realmente precisa.
  * Muito mais leve e controlável.
  * Mambaforge usa `mamba`, um substituto mais rápido para `conda`.

**Miniconda ou Mambaforge é muito mais interessante que Anaconda “cheia”**.

---

## 5. Outros gerenciadores que valem uma menção

### Poetry

Focado em:

* Gerenciar dependências (com `pyproject.toml`).
* Gerar ambiente virtual automaticamente.
* Tratar seu projeto como “pacote” Python (versões, publicação etc.).

Exemplo:

```bash
poetry init        # cria pyproject.toml
poetry add geopandas
poetry shell       # entra no venv gerenciado pelo poetry
```

É ótimo quando você quer projetos bem organizados, replicáveis e “deployáveis”.

### Pipenv

Foi bem popular por um tempo como “pip+virtualenv com esteroides”. Hoje em dia anda menos hype; muita gente migrou pra Poetry. Mas ainda é usado.

---

## 6. Recomendações práticas: Ubuntu vs Windows

Agora a parte mais prática, do tipo “me diz o que usar que eu uso” 😄

### Para Ubuntu

#### Cenário 1: desenvolvimento geral (scripts, web, libs, etc.)

Eu iria de:

* **pyenv + venv** (ou poetry, se quiser dar um passo a mais).

Fluxo recomendado:

1. Instalar `pyenv`.
2. Escolher a versão de Python por projeto:

   ```bash
   pyenv install 3.11.6
   pyenv local 3.11.6
   ```
3. Criar venv:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

Se quiser gerenciamento mais sofisticado de dependências: trocar `pip + requirements.txt` por **Poetry**.

#### Cenário 2: geoprocessamento / data science pesado (GDAL, rasterio, etc.)

Para esse tipo de coisa em Ubuntu, dá pra fazer tanto com `pip` quanto com `conda`, mas **a vida geralmente é mais fácil com `conda`/`mamba`**, especialmente quando começa a brincadeira com dependências nativas.

Sugestão:

* Instalar **Mambaforge (ou Miniconda)**.
* Criar um ambiente específico para o stack geo:

```bash
mamba create -n geo python=3.11 geopandas gdal rasterio shapely pyproj
mamba activate geo
```

Você pode conviver **pyenv+venv** e **conda/mamba** na mesma máquina, sem drama: usa pyenv+venv para apps gerais e conda para os ambientes “pesadões”.

---

### Para Windows

Windows é onde as coisas gostam de ficar divertidas (no sentido caótico).

#### Cenário 1: geoprocessamento / data science

Aqui eu sou bem direto:
**Conda/Miniconda/Mambaforge é fortemente recomendado.**

Instalar GDAL, rasterio, etc. com `pip` puro no Windows é o caminho da penitência, porque envolve compilar ou achar wheels específicas. `conda-forge` já traz tudo pronto.

Fluxo típico:

```powershell
# Depois de instalar Miniconda/Mambaforge
conda create -n geo python=3.11 geopandas gdal rasterio
conda activate geo
```

Se quiser usar Jupyter, QGIS Python, etc., tudo encaixa muito melhor via conda.

#### Cenário 2: desenvolvimento Python mais “puro” (APIs, automação, etc.)

Duas opções boas:

1. **Instalador oficial do Python + venv**

   * Baixa do site do Python, marca “Add to PATH”.
   * Por projeto:

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     pip install -r requirements.txt
     ```

2. **Conda/Miniconda também funcionam bem para isso**

   * Você pode usar conda não só para data science.

`pyenv-win` existe, mas no Windows o ganho é um pouco menor do que no Linux. Se você sente necessidade de trocar muito de versão de Python em Windows, ele é uma opção, mas eu só iria para isso se for realmente preciso.

---

## 7. Resumão bem direto

* **pyenv**

  * Melhor para: escolher versão de Python em **Linux/macOS**.
  * Uso top: em conjunto com `venv` ou `poetry`.

* **venv** (builtin)

  * Melhor para: criar ambientes virtuais simples em qualquer OS.
  * Recomendo como padrão para projetos “normais”.

* **virtualenv**

  * Versão turbo/compatível de `venv`. Útil, mas hoje é menos necessário.

* **conda / Miniconda / Mambaforge / Anaconda**

  * Melhor para: **data science, geoprocessamento, bibliotecas com dependências nativas**, especialmente em **Windows**.
  * Em Ubuntu também é ótimo para o stack pesado (GDAL, etc.).

* **Poetry**

  * Melhor para: quem quer projetos muito organizados, com versionamento de dependências, publicação, etc.

### Minha opinião prática, bem sincera:

* **Ubuntu**

  * Geral: `pyenv + venv` (ou `pyenv + poetry`).
  * Geo / científico pesado: um ambiente separado com **Mambaforge/conda**.

* **Windows**

  * Geo / científico: **Mambaforge/Miniconda + conda-forge**, sem pensar duas vezes.
  * Geral: instalador oficial do Python + `venv` ou também conda, se você gostar do fluxo.

A moral da história: não é escolher “um para governar todos”. É montar um kit de ferramentas onde cada uma resolve bem um pedaço do problema. Python é meio Lego, mesmo.

## Primeiro programa

```python
print('Hello world)'
```