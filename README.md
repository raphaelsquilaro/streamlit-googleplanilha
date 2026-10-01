# 🤖 Agente de IA para Análise de Vendas

Aplicação web desenvolvida em **Python + Streamlit** que permite consultar dados de vendas armazenados em uma **planilha do Google Sheets** utilizando um modelo de **Inteligência Artificial do Google Gemini**.

O usuário visualiza os dados da planilha diretamente na interface e pode fazer perguntas em linguagem natural. A aplicação envia os dados da planilha junto à pergunta para o modelo de IA, que gera uma resposta baseada exclusivamente nas informações disponíveis.

---

## 📌 Visão geral

O projeto integra três componentes principais:

- 📊 **Google Sheets** — fonte dos dados de vendas.
- 🐍 **Python / Pandas** — leitura e processamento dos dados.
- 🤖 **Google Gemini** — análise dos dados e geração das respostas.
- 🖥️ **Streamlit** — interface web da aplicação.

### Fluxo da aplicação

```text
Google Sheets
      │
      ▼
Exportação XLSX
      │
      ▼
Pandas
      │
      ▼
DataFrame
      │
      ├──────────────► Streamlit
      │                    │
      │                    ▼
      │              Usuário faz uma pergunta
      │                    │
      ▼                    ▼
Dados da planilha ──► Google Gemini
                           │
                           ▼
                    Resposta da IA
                           │
                           ▼
                       Streamlit
```

---

## ✨ Funcionalidades

- 📥 Leitura automática de uma planilha do Google Sheets.
- 📊 Visualização dos dados em formato de tabela.
- 💬 Consulta dos dados utilizando linguagem natural.
- 🤖 Integração com a API do Google Gemini.
- 🔎 Respostas baseadas nos dados disponíveis na planilha.
- 🖥️ Interface web simples e interativa através do Streamlit.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| **Python** | Linguagem principal |
| **Streamlit** | Interface web |
| **Pandas** | Leitura e manipulação dos dados |
| **Google Gemini API** | Inteligência Artificial |
| **Google Sheets** | Fonte dos dados |
| **JSON** | Armazenamento das configurações |

---

## 📁 Estrutura do projeto

Uma estrutura recomendada para o projeto é:

```text
.
├── app.py
├── token.json
├── requirements.txt
├── .gitignore
└── README.md
```

### `app.py`

Arquivo principal responsável por executar a aplicação Streamlit, carregar a planilha, receber as perguntas do usuário e consultar o modelo Gemini.

### `token.json`

Arquivo utilizado para armazenar a chave da API do Gemini e o ID da planilha.

> ⚠️ **Importante:** esse arquivo contém informações sensíveis e **não deve ser enviado para um repositório público**.

### `requirements.txt`

Lista das dependências necessárias para executar o projeto.

### `.gitignore`

Deve impedir que informações sensíveis sejam versionadas.

Exemplo:

```gitignore
token.json
.venv/
__pycache__/
*.pyc
.env
```

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

### 2. Crie um ambiente virtual

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install streamlit pandas openpyxl google-genai
```

Ou, caso exista um `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração das credenciais

Crie um arquivo chamado:

```text
token.json
```

Na raiz do projeto.

A estrutura esperada é:

```json
{
    "api_key": "SUA_CHAVE_DA_API",
    "PLANILHA_ID": "ID_DA_SUA_PLANILHA"
}
```

### API Key

A propriedade `api_key` deve conter a chave utilizada para acessar a API do Google Gemini.

### ID da planilha

O `PLANILHA_ID` corresponde ao identificador presente na URL de uma planilha do Google Sheets.

Por exemplo:

```text
https://docs.google.com/spreadsheets/d/SEU_ID_AQUI/edit
```

Nesse caso:

```text
SEU_ID_AQUI
```

é o ID utilizado pela aplicação.

---

## 📊 Configuração da planilha

A aplicação utiliza a URL de exportação do Google Sheets:

```python
url = f"https://docs.google.com/spreadsheets/d/{PLANILHA_ID}/export?format=xlsx"
```

Isso permite que o Pandas carregue a planilha diretamente como um arquivo Excel:

```python
dados = pd.read_excel(url)
```

A planilha deve estar configurada de forma que a aplicação consiga acessá-la.

---

## ▶️ Executando a aplicação

Depois de configurar as dependências e o arquivo `token.json`, execute:

```bash
streamlit run app.py
```

O Streamlit iniciará um servidor local e exibirá uma URL semelhante a:

```text
Local URL: http://localhost:8501
```

Abra essa URL no navegador.

---

## 💬 Como utilizar

Ao abrir a aplicação:

1. Os dados da planilha serão carregados automaticamente.
2. Os dados serão exibidos na interface.
3. Digite uma pergunta no campo de consulta.
4. Clique em **"Pergunte!"**.
5. A pergunta e os dados da planilha serão enviados ao modelo Gemini.
6. A resposta será apresentada na interface.

### Exemplos de perguntas

Considerando uma planilha com informações de vendas, algumas consultas possíveis seriam:

```text
Qual foi o produto mais vendido?
```

```text
Qual vendedor realizou mais vendas?
```

```text
Qual foi o total de vendas?
```

```text
Quais produtos tiveram menor volume de vendas?
```

```text
Qual foi o desempenho de vendas por região?
```

As perguntas devem ser compatíveis com as informações existentes na planilha.

---

## 🧠 Funcionamento da IA

O projeto transforma os dados do DataFrame em texto:

```python
contexto = dados.to_string(index=False)
```

Em seguida, os dados são incorporados ao prompt enviado ao modelo:

```python
prompt = f"""
Você é um agente de análise de vendas.

Responda à pergunta usando SOMENTE os dados da planilha abaixo.

Planilha: {contexto}

Pergunta: {pergunta}

Responda de forma simples e direta.
"""
```

O modelo recebe:

- o contexto da planilha;
- a pergunta realizada pelo usuário;
- a instrução para responder com base nos dados fornecidos.

A resposta retornada pelo modelo é então exibida no Streamlit.

---

## 🔒 Segurança

**Nunca versione credenciais no Git.**

O arquivo:

```text
token.json
```

deve permanecer apenas no ambiente local ou em um mecanismo seguro de gerenciamento de secrets.

Antes de realizar um `git push`, verifique se ele está incluído no `.gitignore`.

Caso uma chave de API seja acidentalmente publicada, ela deve ser considerada comprometida e substituída.

---

## ⚠️ Considerações técnicas

Atualmente, o projeto transforma **toda a planilha em texto** antes de enviá-la ao modelo.

Isso funciona bem para conjuntos de dados pequenos, mas pode apresentar problemas quando a planilha possui muitas linhas ou colunas, como:

- aumento do consumo de tokens;
- maior tempo de processamento;
- aumento do custo da API;
- possibilidade de exceder limites de contexto do modelo;
- respostas menos eficientes em datasets muito grandes.

Para aplicações maiores, pode ser interessante implementar estratégias como:

- filtragem dos dados antes do envio;
- agregações com Pandas;
- seleção das colunas relevantes;
- processamento por partes;
- geração de métricas antes da consulta à IA;
- uso de banco de dados;
- arquitetura baseada em ferramentas/agentes para consultar os dados sob demanda.

---

## 📦 Dependências

Exemplo de `requirements.txt`:

```text
streamlit
pandas
openpyxl
google-genai
```

Instalação:

```bash
pip install -r requirements.txt
```

---

## 🗺️ Próximas melhorias

Algumas evoluções possíveis para o projeto:

- [ ] Adicionar tratamento de erros.
- [ ] Implementar cache para evitar leituras desnecessárias da planilha.
- [ ] Utilizar Streamlit Secrets para armazenar credenciais.
- [ ] Validar a estrutura da planilha antes da análise.
- [ ] Adicionar filtros por período, vendedor e produto.
- [ ] Criar gráficos de vendas.
- [ ] Permitir upload de arquivos Excel/CSV.
- [ ] Melhorar o tratamento de grandes volumes de dados.
- [ ] Adicionar histórico das perguntas realizadas.
- [ ] Implementar autenticação de usuários.
- [ ] Criar testes automatizados.
- [ ] Separar a aplicação em módulos.
- [ ] Adicionar observabilidade e logs.

---

## 📄 Licença

Adicione aqui a licença escolhida para o projeto.

Exemplo:

```text
MIT License
```

---

## 👨‍💻 Autor

**Raphael Campos Squilaro**

Projeto desenvolvido para exploração de **Inteligência Artificial aplicada à análise de dados de vendas**, combinando dados de planilhas, Python e modelos generativos.

---

## ⭐ Contribuições

Contribuições, sugestões e melhorias são bem-vindas.

Para contribuir:

```bash
git checkout -b feature/minha-melhoria
git commit -m "feat: adiciona minha melhoria"
git push origin feature/minha-melhoria
```

Depois, abra um Pull Request no repositório.

---

## 📌 Resumo

Este projeto demonstra uma arquitetura simples para transformar uma planilha de vendas em uma **interface de perguntas e respostas utilizando IA**.

A combinação de **Google Sheets + Pandas + Streamlit + Gemini** permite criar rapidamente aplicações capazes de transformar dados tabulares em informações acessíveis através de linguagem natural.
