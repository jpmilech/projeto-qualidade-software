Feature: Filtro por categoria

  Scenario: Filtrar restaurantes pela categoria Sushi
    Given que o usuário acessa a página inicial
    When selecionar a categoria Sushi
    Then o sistema deve exibir restaurantes relacionados a Sushi

  Scenario: Manter listagem ao remover filtro
    Given que o usuário acessa a página inicial
    When remover o filtro de categoria
    Then o sistema deve exibir todos os restaurantes