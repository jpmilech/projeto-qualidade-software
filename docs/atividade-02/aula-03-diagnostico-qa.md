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