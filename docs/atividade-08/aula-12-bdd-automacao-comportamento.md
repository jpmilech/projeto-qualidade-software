# Aula 12 – BDD e Automação Orientada a Comportamento

## Integrante
João Pedro Milech

---

# 1. Fluxo escolhido

## Filtro por categoria

### O que faz
Permite filtrar restaurantes por categoria.

### Importância
Melhora a experiência do usuário e facilita a busca.

### Cenários esperados
- Filtro aplicado corretamente
- Lista atualizada
- Categoria destacada

---

# 2. Cenários BDD

## Feature: Filtro por categoria

### Scenario: Filtrar restaurantes pela categoria Sushi

Given que o usuário acessa a página inicial

When selecionar a categoria Sushi

Then o sistema deve exibir restaurantes relacionados a Sushi

---

### Scenario: Manter listagem ao remover filtro

Given que o usuário acessa a página inicial

When remover o filtro de categoria

Then o sistema deve exibir todos os restaurantes

---

# 3. Implementação da automação

## Tecnologias utilizadas
- Python
- pytest
- pytest-bdd
- Playwright

## Estrutura do projeto

```text
features/
tests/
evidencias/
```

## Automação implementada

O teste automatizado acessa o sistema LocalEats utilizando Playwright e valida o comportamento esperado descrito nos cenários BDD.

---

# 4. Execução dos testes

## Resultado

- Total de cenários: 2
- Cenários aprovados: 2
- Cenários com falha: 0

## Evidências

As evidências da execução estão disponíveis na pasta `evidencias/`.

---

# 5. Análise crítica

## O cenário escrito ficou compreensível?

Sim. Os cenários ficaram simples e objetivos.

## O teste automatizado ficou legível?

Sim. A separação entre Given, When e Then facilitou o entendimento.

## O BDD ajudou a entender o comportamento?

Sim. O comportamento esperado ficou mais claro.

## Quais dificuldades surgiram?

A principal dificuldade foi configurar o ambiente do Playwright e ajustar os seletores da interface.

## Os seletores foram frágeis?

Sim. Alguns elementos da interface dificultaram a automação.

## O teste ficou dependente da interface?

Parcialmente, pois depende do carregamento da página.

## O cenário representa uma regra de negócio?

Sim. O filtro por categoria é importante para navegação do usuário.

## O que tornaria o teste mais robusto?

Utilizar seletores mais específicos e validar elementos reais da interface.

---

# 6. Reflexão no contexto do LocalEats

## BDD melhora a comunicação entre equipe?

Sim. O BDD aproxima desenvolvimento, qualidade e negócio.

## Todo teste deve ser escrito em BDD?

Não. O BDD é mais útil para fluxos importantes e comportamentos de negócio.

## Quando vale a pena usar BDD?

Quando é necessário descrever comportamentos de forma clara para toda a equipe.

## O comportamento ficou mais claro?

Sim. A linguagem Gherkin facilitou a compreensão.

## Como isso ajuda no projeto do grupo?

Ajuda a documentar funcionalidades e validar comportamentos automaticamente.