from playwright.sync_api import expect

from src.PBL07.pages.login_page import LoginPage
from src.PBL07.pages.home_page import HomePage


def test_navegacao_restaurante(page):

    login = LoginPage(page)

    home = HomePage(page)

    login.acessar()

    login.realizar_login(
        "joaoEats@gmail.com",
        "joao123"
    )

    restaurante = page.locator(
        'a[href="restaurant.html?id=2"]'
    )

    expect(restaurante).to_be_visible()

    home.abrir_restaurante()

    expect(page).to_have_url(
        "https://local-eats-unisenac.vercel.app/static/restaurant.html?id=2"
    )

    import re
from playwright.sync_api import Playwright, sync_playwright, expect


#def run(playwright: Playwright) -> None:
#    browser = playwright.chromium.launch(headless=False)
#    context = browser.new_context()
#    page = context.new_page()
#    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
#    page.get_by_role("textbox", name="teste@teste.com").click()
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").fill("joao")
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").fill("joaoE")
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").fill("joaoEats@gmail.com")
#    page.get_by_role("textbox", name="teste@teste.com").press("Tab")
#    page.get_by_role("textbox", name="Sua senha secreta").fill("joao123")
#    page.get_by_role("textbox", name="Sua senha secreta").press("Enter")
#    page.get_by_role("textbox", name="Sua senha secreta").press("Tab")
#    page.locator("#loginForm").get_by_role("button", name="Entrar").press("Enter")
#    page.locator("#loginForm").get_by_role("button", name="Entrar").press("Enter")
#    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
#    page.get_by_role("link", name="Restaurante Sabor 1 Restaurante Sabor 1 $$  Japonesa  Centro Um ótimo lugar").click()#

    # ---------------------
#    context.close()
#    browser.close()


#with sync_playwright() as playwright:
#    run(playwright)