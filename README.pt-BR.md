# DevLens

[![CI](https://github.com/JoaoAlves20/DevLens/actions/workflows/ci.yml/badge.svg)](https://github.com/JoaoAlves20/DevLens/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)
[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)](LICENSE)

[English](README.md) · **Português**

> Análise estática de engenharia para repositórios de código.

O DevLens recebe um repositório Git (URL pública ou caminho local) e gera um relatório
técnico sobre ele: como está estruturado, com o que foi construído, onde a arquitetura
é frágil, que código está duplicado, quais dependências têm vulnerabilidades e o que
melhorar primeiro.

**Não é um chatbot que lê código.** Cada achado vem de análise determinística
(parsing, grafos de dependência, hashing e métricas), sempre aponta o arquivo e a linha
exatos, e a mesma entrada sempre gera o mesmo relatório.

> **Status:** em desenvolvimento inicial (v0.0.1). Veja o [roadmap](#roadmap).

## Funcionalidades planejadas

| Área | O que o DevLens reporta |
|---|---|
| **Estrutura** | Árvore de diretórios, linhas de código por linguagem, maiores arquivos, higiene do projeto (testes, CI, docs) |
| **Tecnologias** | Linguagens, frameworks, ferramentas de build, CI e containers detectados pelos manifests |
| **Arquitetura** | Grafo de dependências, dependências circulares, god modules, instabilidade, complexidade, violações de camadas |
| **Rails** | Grafo de dependências inferido pelas convenções do Zeitwerk, controllers e models inchados, versões do Rails sem suporte |
| **Duplicação** | Código copiado e colado, inclusive com identificadores renomeados |
| **Diagramas** | Diagramas de arquitetura em Mermaid e Graphviz, e um grafo interativo |
| **Dependências** | Vulnerabilidades conhecidas (OSV.dev), pacotes desatualizados, licenças |
| **Relatório** | Health score, achados priorizados com evidência, exportação em JSON, Markdown, HTML e SARIF |

Linguagens suportadas na v1: **Python**, **JavaScript / TypeScript** e **Ruby on Rails**.
Outras linguagens podem ser adicionadas como plugins.

## Formas de uso

```bash
devlens analyze https://github.com/owner/repo   # relatório na CLI (a partir do Dia 2)
devlens serve                                   # interface web local (a partir do Dia 13)
```

A GitHub Action vai comentar nos pull requests a variação do health score.
Tudo roda localmente: não existe serviço hospedado. Uma demo estática com relatórios
pré-gerados será publicada no GitHub Pages.

## Desenvolvimento

Requer o [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/JoaoAlves20/DevLens.git
cd DevLens
uv sync                       # cria o virtualenv e instala as dependências
uv run pre-commit install     # roda lint e checagem de tipos antes de cada commit

uv run devlens --version
uv run pytest                 # testes + cobertura
uv run ruff check .           # lint
uv run mypy                   # checagem de tipos estrita
```

## Como este projeto é construído

O DevLens é construído por **João Alves, atuando como dono do projeto e orquestrador de
IA**, com o Claude como implementador. Todas as decisões de produto e de arquitetura
são do dono e ficam registradas:

- [AI_WORKFLOW.md](AI_WORKFLOW.md): papéis, regras e o ciclo de cada sessão
- [DECISIONS.md](DECISIONS.md): registro de todas as decisões
- [docs/adr/](docs/adr/): registros de decisões de arquitetura (ADRs)

## Roadmap

| Fase | Marco | Conteúdo |
|---|---|---|
| 1. Engine e CLI | v0.1.0 | Ingestão, estrutura e detecção de tecnologias |
| | v0.2.0 | Grafos de imports (Python, JS/TS, Ruby/Zeitwerk), métricas de arquitetura, regras de camadas, diagramas Mermaid |
| | v0.3.0 | Duplicação, dependências e vulnerabilidades, health score, relatórios |
| 2. Interface web local | v0.4.0 | `devlens serve`, dashboard, explorador de achados, grafo interativo |
| 3. Lançamento | v1.0.0 | GitHub Action, hotspots, demo estática, publicação no PyPI |

## Licença

[MIT](LICENSE)
