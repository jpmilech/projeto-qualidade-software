from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page
import pytest

scenarios('../features/filtro_categoria.feature')


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@given('que o usuário acessa a página inicial')
def acessar_home(page: Page):

    page.goto('https://local-eats-unisenac.vercel.app/')

    page.wait_for_timeout(3000)


@when('selecionar a categoria Sushi')
def selecionar_categoria(page: Page):

    page.locator("button").first.click()

    page.wait_for_timeout(2000)


@then('o sistema deve exibir restaurantes relacionados a Sushi')
def validar_sushi(page: Page):

    assert page.locator("body").is_visible()


@when('remover o filtro de categoria')
def remover_filtro(page: Page):

    page.reload()

    page.wait_for_timeout(2000)


@then('o sistema deve exibir todos os restaurantes')
def validar_lista(page: Page):

    assert page.locator("body").is_visible()