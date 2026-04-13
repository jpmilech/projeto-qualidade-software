1. Funcionalidades principais
Busca de restaurantes (por tipo, localização e preço)
Visualização de restaurantes (cardápio, fotos e avaliações)
Sistema de avaliações
Favoritar restaurantes
Recomendações personalizadas

2. Níveis de teste
2.1 Busca de restaurantes
Teste unitário: Validação dos filtros (tipo, localização, preço)
Teste de integração: Comunicação entre frontend, API e banco de dados
Teste de sistema: Fluxo completo de busca retornando resultados corretos
Teste de aceitação: Usuário consegue encontrar restaurantes conforme critérios

2.2 Visualização de restaurantes
Teste unitário: Renderização de dados (nome, cardápio, imagens)
Teste de integração: API + banco de dados fornecendo informações corretas
Teste de sistema: Abertura da página com todos os dados carregados corretamente
Teste de aceitação: Usuário visualiza informações completas do restaurante

2.3 Sistema de avaliações
Teste unitário: Criação e validação de avaliações
Teste de integração: Salvamento e recuperação das avaliações no banco
Teste de sistema: Usuário envia avaliação e ela aparece corretamente
Teste de aceitação: Usuário consegue avaliar e visualizar avaliações

2.4 Favoritar restaurantes
Teste unitário: Adição e remoção de favoritos
Teste de integração: Persistência dos favoritos no banco de dados
Teste de sistema: Usuário salva e acessa lista de favoritos
Teste de aceitação: Usuário consegue gerenciar seus favoritos

2.5 Recomendações personalizadas
Teste unitário: Lógica de recomendação
Teste de integração: Uso de dados do usuário + histórico
Teste de sistema: Exibição de recomendações na interface
Teste de aceitação: Usuário recebe sugestões relevantes

3. Prioridades e riscos
Funcionalidades mais críticas:
Busca de restaurantes
Sistema de avaliações
Visualização de restaurantes
Justificativa:
Busca: é a principal funcionalidade do sistema. Se falhar, o sistema perde utilidade.
Avaliações: impacta diretamente a confiança dos usuários. Perda de dados é crítica.
Visualização: sem exibir informações corretamente, o usuário não consegue tomar decisões.
Maior impacto de erro:
Resultados incorretos → prejudica a credibilidade
Perda de avaliações → perda de confiança
Lentidão → abandono da plataforma

4. Pirâmide de testes
Maior concentração:
Testes unitários
Mais rápidos e baratos
Detectam erros cedo
Quantidade média:
Testes de integração
Garantem comunicação entre componentes
Menor quantidade:
Testes de sistema e aceitação
Mais caros e lentos
Usados para validar fluxos críticos
Justificativa:

A estratégia segue a pirâmide de testes para reduzir custo e aumentar eficiência, priorizando testes rápidos e automatizáveis nas camadas mais baixas.

5. Testes em produção
Deve usar?

Sim, com controle.

Situações:
Monitoramento de desempenho (horários de pico)
Testes A/B de interface
Coleta de erros reais (logs e métricas)
Justificativa:

Testes em produção ajudam a identificar problemas reais que não aparecem em ambiente de teste, principalmente relacionados a carga, dispositivos e comportamento do usuário.