# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software  
> Aula 3 – Papéis, Responsabilidades e Práticas de QA  
> Equipe: [Nome da equipe]  
> Integrantes: [João Marcelo Bitar, João Pedro Milech, Enzo Sabbado]

# 1. Diagnóstico da Situação Atual:


## 1.1 Papéis atuais identificados
- Gerente de produto;
- UX/UI designer;
- Analista de sistemas;
- Desenvolvedores front e back-end;
- DevOps;

---

## 1.2 Quem é responsável pela qualidade hoje?
> Os responsáveis técnicos provavelmente são os próprios devs, ou nem mesmo eles. O gerente de produto deveria garantir a qualidade como gestor, mas não tem o know-how técnico para debugar a aplicação.

---

## 1.3 Problemas identificados
- Ausência de um responsável claro pela qualidade;
- Falta de processos de teste estruturados;
- Entrega de funcionalidades sem validação adequada;
- Comunicação falha entre equipe técnica e gestão;
- Possível ausência de testes automatizados e manuais;


---

## 1.4 Impactos desses problemas    
>Isso acarreta em bugs frequentes(ex: falha ao finalizar pedidos) e features não funcionando exatamente como deveriam(Pedidos duplicados), o que causa mais custo de manutenção e retrabalho do time.

---

## 1.5 A qualidade é responsabilidade de quem?
>A qualidade de software deve ser responsabilidade de toda a equipe levando em conta seus respectivos papeis dentro do desenvolvimento do prouto. Apesar disso, o QA é especializado nisso, e garante uma segurança melhor de uma qualidade satisfatória

---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Desenvolvedor;
- QA / Analista de Qualidade;
- Analista de Sistemas;
- DevOps;

---

## 2.2 Descrição dos papéis

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|------|------|
| Desenvolvedor | Desenvolver a aplicação; implementar funcionalidades; corrigir bugs | É o primeiro responsável pela qualidade do código; pode criar testes automatizados; deve garantir que a funcionalidade funcione corretamente antes de entregar |
| QA / Analista de Qualidade | Planejar e executar testes; identificar e registrar defeitos; validar funcionalidades antes do deploy | Garante que o sistema atenda aos requisitos; previne que bugs cheguem à produção; assegura a qualidade do produto |
| Analista de Sistemas | Levantar e documentar requisitos; definir critérios de aceitação | Requisitos mal definidos geram erros no sistema; ajuda a evitar retrabalho e falhas de entendimento |
| DevOps | Gerenciar deploy e infraestrutura; monitorar o sistema em produção | Garante estabilidade do ambiente; evita erros no processo de entrega; pode impedir deploy de código com falhas |

# 3. Práticas de QA Sugeridas

## 3.1 Lista de práticas

- Testes manuais das funcionalidades principais;
- Testes exploratórios;
- Registro e acompanhamento de bugs;
- Revisão de funcionalidades antes do deploy;

---

## 3.2 Explicação das práticas

### Prática 1:
> Descrição: Realizar testes manuais nas funcionalidades mais críticas do sistema, como o fluxo de pedidos, garantindo que elas funcionem corretamente antes de serem disponibilizadas para o usuário.

### Prática 2:
> Descrição: Aplicar testes exploratórios, onde o QA navega livremente pelo sistema com o objetivo de encontrar erros inesperados que não foram previstos nos testes formais.

### Prática 3:
> Descrição: Registrar e acompanhar bugs em uma ferramenta de gestão, organizando os defeitos encontrados, seus status e prioridades, facilitando o controle e a correção dos problemas.

### Prática 4:
> Descrição: Realizar uma validação final das funcionalidades antes do deploy (QA Gate), garantindo que nenhuma funcionalidade seja enviada para produção sem passar por uma verificação de qualidade.

---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – Analista de Qualidade (QA)

### Descrição da vaga
> A Local Eats busca um Analista de Qualidade(QA) para garantir a estabilidade e confiabilidade da plataforma. O profissional será responsável por estruturar processos de teste e assegurar que as funcionalidades entregues estejam de acordo com os requisitos.

### Responsabilidades
- Planejar e executar testes manuais e exploratórios;
- Identificar, registrar e acompanhar bugs;
- Validar funcionalidades antes do deploy;

### Requisitos obrigatórios
- Conhecimento básico em testes de software;
- Capacidade de análise e atenção a detalhes;
- Boa comunicação com equipe técnica;

### Requisitos desejáveis
- Experiência com ferramentas de gestão de bugs (ex: Trello, Jira);
- Conhecimento básico em testes automatizados;
- Familiaridade com metodologias ágeis;

### Certificações desejáveis
- CTFL (Certified Tester Foundation Level);

---

## 4.2 Vaga 2 – Engenheiro DevOps

### Descrição da vaga
> A Local Eats busca um(a) profissional DevOps para estruturar e automatizar o processo de entrega da aplicação, garantindo maior estabilidade, segurança e qualidade no deploy.

### Responsabilidades
- Gerenciar infraestrutura e processos de deploy;
- Monitorar o sistema em produção;

### Requisitos obrigatórios
- Conhecimento em Git e versionamento de código;
- Noções de infraestrutura e deploy de aplicações;
- Experiência com ambientes Linux;

### Requisitos desejáveis
- Conhecimento em Docker e containers;
- Experiência com serviços em nuvem;

### Certificações desejáveis
- CTFL (Certified Tester Foundation Level);
- AWS Certified Cloud Practitioner;


# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> Aprendemos como funciona na prática a designação de papéis relacionados a qualidade de software dentro do desenvolvimento de um produto e como as responsabilidades relacionadas à qualidade se diluem dentro da equipe. Atribuir funções objetivas para os componentes da equipe, e algumas questões e conceitos específicos ainda estavam meio nebulosos. A principal questão é a total ausência de responsáveis pela qualidade do software no time de desenvolvimento, por isso nossas propostas se baseiam em preencher essa lacuna contratando profissionais qualificados e adotando processos dentro da construção do produto que assegurem a qualidade.

---

# 📌 Observações (opcional)

