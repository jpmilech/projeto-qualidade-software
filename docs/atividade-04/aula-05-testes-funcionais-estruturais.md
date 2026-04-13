Testes Funcionais vs Estruturais — Local Eats

1. Funcionalidade escolhida: Busca de restaurantes
Descrição

A funcionalidade de busca permite que o usuário encontre restaurantes com base em critérios como tipo de culinária, localização e faixa de preço.

Expectativa do usuário

O usuário espera:

Receber resultados corretos e relevantes
Ter respostas rápidas
Conseguir filtrar facilmente
Não encontrar erros ou inconsistências

2. Testes Caixa-Preta (Visão do Usuário)
Entradas possíveis
Tipo de culinária (ex: japonesa, italiana)
Localização (bairro, cidade)
Faixa de preço
Combinação de filtros
Campos vazios ou inválidos
Comportamentos esperados
Retornar restaurantes compatíveis com os filtros
Exibir lista corretamente organizada
Não apresentar erros visuais ou falhas
Responder rapidamente
Situações de erro
Resultados incorretos ou irrelevantes
Nenhum resultado quando deveria haver
Lentidão excessiva
Falha ao aplicar filtros
Interface quebrada ou confusa

3. Testes Caixa-Branca (Visão do Sistema)
Possível implementação
Uso de consultas ao banco de dados com filtros
Estruturas condicionais (if/else) para aplicar filtros
Validação de entradas do usuário
Algoritmo de ordenação ou relevância
Estruturas lógicas e regras
Verificação se os campos estão preenchidos
Combinação de múltiplos filtros
Tratamento de dados inválidos
Controle de exceções (erros de consulta, dados nulos)
Situações a serem testadas no código
Todos os caminhos possíveis das condições (if/else)
Casos com dados nulos ou vazios
Erros no banco de dados
Performance da consulta
Integração entre backend e banco

4. Comparação entre as abordagens
Diferença principal
Caixa-preta: testa o sistema do ponto de vista do usuário, sem conhecer o código
Caixa-branca: testa a lógica interna do sistema, com acesso ao código
Tipos de problemas identificados
Caixa-preta:
Erros de funcionalidade
Problemas de usabilidade
Resultados incorretos
Caixa-branca:
Falhas na lógica interna
Caminhos de código não testados
Problemas de validação e regras

5. Reflexão no contexto do LocalEats
Abordagem mais útil

Ambas são essenciais.

Caixa-preta ajuda a identificar problemas já relatados pelos usuários, como:
Resultados incorretos
Dificuldade de uso
Caixa-branca permite identificar a causa desses problemas, como:
Erros na lógica de filtros
Falhas na implementação
Apenas uma abordagem é suficiente?

Não.

Justificativa

Os problemas do sistema envolvem tanto:

Experiência do usuário (interface, usabilidade)
Quanto falhas internas (lógica, integração, performance)

Portanto, é necessário combinar as duas abordagens para garantir qualidade completa do sistema.