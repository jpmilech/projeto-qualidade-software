class RestaurantPage:

    def __init__(self, page):
        self.page = page

    def validar_restaurante(self):

        return self.page.get_by_role(
            "heading",
            name="Restaurante Sabor"
        )

    def validar_cardapio(self):

        return self.page.get_by_role(
            "heading",
            name="Prato Especial 0"
        )