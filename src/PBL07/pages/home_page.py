class HomePage:

    def __init__(self, page):
        self.page = page

    def abrir_restaurante(self):

        self.page.locator(
            'a[href="restaurant.html?id=2"]'
        ).click()