# Aula 15 – Modelos de Maturidade – LocalEats

**Unidade Curricular:** Qualidade de Software
**Professor:** Luciano Zanuz
**Curso:** ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet
**Sistema avaliado:** LocalEats (https://local-eats-unisenac.vercel.app/)

---

## 1. Diagnóstico de Maturidade

> Diagnóstico atualizado com base no mapeamento formal do processo (fluxograma e tabela de entradas/atividades/saídas produzidos pela equipe na atividade anterior), somado às práticas relatadas informalmente.

| Critério | Sim | Parcial | Não |
|---|---|---|---|
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | | | X |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | | X |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | | X |
| Existe padronização para implementação de funcionalidades? | X | | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | X | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | | X | |
| Os artefatos do projeto (requisitos, testes, código) são organizados e versionados? | | X | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | | X |
| A equipe realiza reuniões ou momentos de retrospectiva para identificar melhorias? | | | X |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | X |

### Classificação do processo: **Inicial (em transição para Gerenciado)**

### Justificativa

O mapeamento do processo (fluxograma + tabela de entradas/atividades/saídas) traz uma evidência importante que muda a leitura inicial: o fluxo de desenvolvimento **existe, é documentado e é seguido por toda a equipe** — a própria equipe confirma isso na reflexão ("todos seguem o mesmo fluxo"). Isso indica que o processo já deixou de ser puramente ad hoc: há uma sequência padronizada (demanda → requisitos → desenvolvimento → testes → correção → entrega) aplicada de forma repetível a todas as funcionalidades, incluindo um ciclo de teste-correção formalizado no próprio diagrama.

Por outro lado, faltam os elementos de **gestão** que caracterizam plenamente o nível Gerenciado do CMMI/MPS.BR: não há controle de mudanças, os defeitos encontrados não são registrados em nenhum artefato (apenas corrigidos), não existe rastreabilidade entre requisito e funcionalidade entregue, as tarefas não são planejadas nem acompanhadas com uma ferramenta, e não há métricas de qualidade nem reuniões de retrospectiva. Também há uma inconsistência a observar: a revisão de código por outro integrante, mencionada pela equipe, não aparece como etapa no fluxograma mapeado — ou essa prática deveria ser incluída formalmente no processo, ou ela ocorreu de forma pontual e ainda não está institucionalizada.

Por isso, classificamos o processo como **Inicial, em transição para Gerenciado**: o "o quê" do processo já está definido e comunicado, mas o "como gerenciar" (planejamento, controle de mudança, registro de defeitos, métricas) ainda não foi implementado, o que impede o processo de ser considerado plenamente Gerenciado.

---

## 2. Identificação de Lacunas

| Lacuna | Impacto |
|---|---|
| O fluxo mapeado não prevê registro de defeitos (o erro é corrigido, mas não fica documentado) | Perde-se o histórico de problemas recorrentes, impossibilitando medir a qualidade ao longo do tempo ou identificar padrões de falha |
| Ausência de controle de mudanças no processo | Alterações de escopo ou requisitos no meio do desenvolvimento não são tratadas, aumentando o risco de retrabalho e inconsistências |
| Falta de rastreabilidade entre requisito e funcionalidade entregue | Mesmo com o fluxo definido, não há como comprovar que tudo que foi solicitado foi de fato implementado e testado |
| Inconsistência entre o processo mapeado e a prática relatada (revisão de código não aparece no fluxograma) | Gera dúvida sobre se a revisão realmente acontece sempre ou apenas ocasionalmente, o que é um risco para a confiabilidade do processo |
| Ausência de reuniões de acompanhamento e retrospectiva | A equipe perde a oportunidade de identificar problemas recorrentes no próprio fluxo e evoluí-lo de forma contínua |
| Falta de indicadores/métricas de qualidade | Impossibilita medir objetivamente a evolução da qualidade do produto e do processo, dificultando decisões baseadas em dados |

---

## 3. Propostas de Melhoria

| Melhoria | Benefício |
|---|---|
| Incluir formalmente uma etapa de registro de defeitos no fluxograma (ex.: planilha ou Issues do GitHub vinculadas ao erro encontrado nos testes) | Cria histórico de qualidade e permite gerar indicadores simples (nº de bugs por entrega, tempo médio de correção) |
| Atualizar o fluxograma para incluir a etapa de revisão de código como parte oficial do processo, com Pull Request obrigatório antes do merge | Resolve a inconsistência entre processo mapeado e prática real, e institucionaliza uma boa prática que já existe informalmente |
| Adotar uma ferramenta de gestão de tarefas (GitHub Projects ou Trello), vinculando cada requisito a uma tarefa e à funcionalidade correspondente | Cria rastreabilidade entre requisito e entrega, além de permitir planejamento e acompanhamento regular das tarefas |
| Instituir uma etapa simples de controle de mudanças (registro de qualquer alteração de requisito já em desenvolvimento) | Reduz retrabalho e torna visível o impacto de mudanças de escopo durante o desenvolvimento |
| Realizar uma retrospectiva curta ao final de cada entrega, revisando o próprio fluxograma do processo | Transforma o processo mapeado em algo vivo, que evolui com base na experiência da equipe, aproximando o time do nível Definido |

---

## Considerações finais

A equipe do LocalEats está em transição entre os níveis **Inicial** e **Gerenciado** de maturidade. O ponto forte é que o processo já foi mapeado, documentado e é reconhecidamente seguido por todos — isso é um avanço real em relação a um processo puramente informal. O que falta para consolidar o nível Gerenciado é adicionar a "camada de gestão" ao redor do fluxo já existente: registro de defeitos, controle de mudanças, rastreabilidade e planejamento/acompanhamento de tarefas. A boa notícia é que isso não exige reformular o processo do zero — basta enriquecer o fluxograma já criado com essas etapas de gestão, o que tende a gerar o maior ganho de maturidade com o menor esforço de implementação.