# Portfólio de Estudos em SGBD

Repositório pessoal de estudos e práticas da disciplina de **Sistemas de Gerenciamento de Banco de Dados (SGBD)**.

Meu nome é **João Pedro da Costa Rezende**, sou estudante de TI na **PUC**, e utilizo este espaço para documentar minha evolução acadêmica em Banco de Dados, organizar consultas úteis e registrar exercícios práticos com foco em **SQL Server** e **modelagem de dados**.

Este repositório está em constante evolução. A cada novo tópico estudado, busco registrar scripts, exemplos, anotações e práticas que ajudem a consolidar conceitos fundamentais de SGBD.

## Tecnologias Utilizadas

- **SQL Server**: principal SGBD utilizado nos scripts e exercícios.
- **T-SQL**: linguagem SQL aplicada aos recursos específicos do SQL Server.
- **SQL Server Management Studio (SSMS)** ou **Azure Data Studio**: ferramentas recomendadas para executar e testar os scripts.
- **Git e GitHub**: versionamento, organização do histórico de estudo e publicação do portfólio.
- **Python**: apoio em automações simples de manutenção do repositório.
- **Markdown**: documentação dos exercícios, revisões e observações.

## Estrutura do Repositório

| Pasta | Conteúdo estudado |
| --- | --- |
| `01_Databases/` | Scripts de criação de bancos, tabelas, cargas iniciais e bases de apoio para os exercícios. Aqui pratico DDL, DML e organização de esquemas. |
| `02_Introduction/` | Conceitos iniciais de SQL, consultas básicas, comentários, boas práticas e primeiros comandos de seleção. |
| `03_FilterAndOrder/` | Filtros com `WHERE`, operadores lógicos, `LIKE`, `IN`, `BETWEEN`, tratamento de nulos e ordenação com `ORDER BY`. |
| `04_Aggregated/` | Funções agregadas como `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`, além de `GROUP BY` e `HAVING`. |
| `05_Sequence/` | Uso de sequências no SQL Server para geração controlada de valores numéricos. |
| `06_Regex/` | Estudos sobre padrões textuais, validações e recursos relacionados a strings e collation. |
| `07_Queries/` | Consultas variadas, CRUD, transações, constraints, estruturas condicionais e exemplos práticos de manipulação de dados. |
| `08_SubQueries/` | Subconsultas em diferentes contextos, incluindo `EXISTS`, `FROM`, operadores `ANY`, `SOME` e `ALL`. |
| `09_Variables/` | Tipos de dados, variáveis, conversões, formatação, funções matemáticas e variáveis globais. |
| `10_With/` e `18_WITH_CTES/` | Common Table Expressions (CTEs), consultas nomeadas, múltiplas CTEs e uso de CTEs em cenários agregados. |
| `11_Strings/` | Manipulação de textos, funções de string e tratamento de valores textuais. |
| `12_Dates/` | Operações com datas, formatação e funções temporais. |
| `13_Views/` | Criação e uso de views para abstrair consultas e organizar regras de leitura. |
| `14_functions/` | Functions no SQL Server, encapsulando lógica reutilizável dentro do banco. |
| `15_Procedures/` | Stored procedures para execução de rotinas e consultas parametrizadas. |
| `16_TriggersDML/` | Triggers ligadas a operações DML, como `INSERT`, `UPDATE` e `DELETE`. |
| `17_TriggersDDL/` | Triggers para eventos DDL, úteis para auditoria e controle de alterações estruturais. |
| `19_WindowFunctions/` | Funções de janela, rankings, particionamento, acumulados, médias móveis e comparações temporais. |
| `20_Conditionals/` | Estruturas condicionais e expressões de decisão aplicadas a consultas. |
| `97_Diagrams/` | Diagramas e modelos de dados usados para praticar modelagem, relacionamentos e leitura de DERs. |
| `98_Review/` | Material de revisão e consolidação dos principais tópicos estudados. |
| `99_exercises/` | Exercícios práticos organizados por desafio, com foco em fixação e evolução incremental. |
| `scripts/` | Automações de apoio para manutenção do repositório. |

## Como Executar os Scripts Localmente

1. Instale ou tenha acesso a uma instância do **SQL Server**.
2. Abra o **SQL Server Management Studio (SSMS)** ou o **Azure Data Studio**.
3. Crie ou selecione um banco de dados de estudo.
4. Execute primeiro os scripts de estrutura, normalmente arquivos `DDL.sql`.
5. Execute os scripts de carga, geralmente arquivos `insert`, `inserts` ou `DML.sql`.
6. Rode os scripts de consultas conforme o tópico estudado.

Exemplo de fluxo:

```sql
-- 1. Criar estrutura
-- Execute: 01_Databases/ecommerce/DDL.sql

-- 2. Inserir dados
-- Execute: 01_Databases/ecommerce/insertsECommerce.sql

-- 3. Praticar consultas
-- Execute scripts das pastas 03_FilterAndOrder, 04_Aggregated, 08_SubQueries etc.
```

Também é possível executar scripts via terminal com `sqlcmd`, quando disponível:

```bash
sqlcmd -S localhost -d NomeDoBanco -E -i caminho/do/script.sql
```

Para autenticação com usuário e senha:

```bash
sqlcmd -S localhost -d NomeDoBanco -U seu_usuario -P sua_senha -i caminho/do/script.sql
```

## Script de Limpeza de Cabeçalhos

O repositório possui um script Python para padronizar comentários de autoria em arquivos `.sql`:

```bash
python3 scripts/clean_sql_headers.py
```

Por padrão, ele percorre todos os arquivos `.sql` do repositório e substitui linhas de comentário que mencionem autoria original por:

```sql
-- Desenvolvido/Adaptado por João Pedro da Costa Rezende
```

Antes de executar em massa, recomendo conferir as alterações com:

```bash
git diff
```

## Padrão de Commits

Vou utilizar **Conventional Commits** para manter o histórico claro e fácil de acompanhar.

Formato:

```text
tipo(escopo): descrição curta no imperativo
```

Tipos recomendados:

- `feat`: novo exercício, script ou tópico de estudo.
- `fix`: correção em consulta, modelagem, carga ou documentação.
- `docs`: mudanças em README, anotações ou explicações.
- `refactor`: reorganização de scripts sem alterar o objetivo do exercício.
- `test`: validações, consultas de conferência ou scripts de verificação.
- `chore`: manutenção do repositório, renomeação de arquivos ou ajustes de estrutura.

Exemplos:

```text
docs(readme): personaliza apresentação do portfólio de sgbd
feat(queries): adiciona exercícios de filtros com where
feat(aggregations): adiciona consultas com group by e having
feat(modelagem): adiciona der do cenário de vendas
fix(subqueries): corrige comparação com operador exists
refactor(databases): reorganiza scripts ddl e inserts
chore(scripts): adiciona limpeza de cabeçalhos sql
```

## Objetivo de Aprendizado

Meu objetivo com este portfólio é construir uma base sólida em SGBD, praticando desde comandos fundamentais de SQL até tópicos mais avançados como procedures, triggers, views, CTEs e window functions.

Além de servir como material de revisão, este repositório demonstra minha evolução prática na disciplina e minha capacidade de organizar conhecimento técnico de forma versionada e documentada.
